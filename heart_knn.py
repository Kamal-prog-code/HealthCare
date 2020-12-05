from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession
from pyspark.ml.feature import StandardScaler
from pyspark.mllib.evaluation import BinaryClassificationMetrics
import pickle
import numpy as np
import os

spark = SparkSession.builder.appName('HSP').getOrCreate()
df=spark.read.csv('hdfs://localhost:9000/user/BigDataProj/heart_failure_clinical_records_dataset.csv',inferSchema=True,header=True)

from pyspark.sql.functions import col
from sklearn.neighbors import KNeighborsClassifier
new_data = df.select(*(col(c).cast("float").alias(c) for c in df.columns))

from pyspark.sql.functions import col,count,isnan,when
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
new_data.select([count(when(col(c).isNull(),c)).alias(c) for c in new_data.columns]).show()

cols=new_data.columns
cols.remove("DEATH_EVENT")
assembler = VectorAssembler(inputCols=cols,outputCol="features")

data=assembler.transform(new_data)
# data.select("features",'Outcome').show(truncate=False)


train, tesT = new_data.randomSplit([0.7, 0.3])
x_col = new_data.columns
x_train = train.toPandas()[x_col[:-1]].values
y_train = train.toPandas()['DEATH_EVENT'].values

knncls = KNeighborsClassifier()
knncls.fit(x_train,y_train)
param_grid = {'n_neighbors': np.arange(1, 25)}
knn_gscv = GridSearchCV(knncls, param_grid, cv=10)

knn_gscv.fit(x_train, y_train)
final_k=knn_gscv.best_params_['n_neighbors']

final_model=KNeighborsClassifier(n_neighbors=final_k)
final_model.fit(x_train,y_train)

save_path = 'prediction/'
completeName = os.path.join(save_path, "heartknn.pkl")         
pickle.dump(final_model, open(completeName, 'wb'))

























