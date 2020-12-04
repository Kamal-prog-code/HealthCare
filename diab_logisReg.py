from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession
from pyspark.ml.feature import StandardScaler
from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.evaluation import BinaryClassificationMetrics
from pyspark.ml.classification import RandomForestClassifier
import pickle
import os

spark = SparkSession.builder.appName('HSP').getOrCreate()
df=spark.read.csv('media/diab.csv',inferSchema=True,header=True)

from pyspark.sql.functions import col
from sklearn.linear_model import LogisticRegression
new_data = df.select(*(col(c).cast("float").alias(c) for c in df.columns))

from pyspark.sql.functions import col,count,isnan,when
from sklearn.preprocessing import StandardScaler
new_data.select([count(when(col(c).isNull(),c)).alias(c) for c in new_data.columns]).show()

cols=new_data.columns
cols.remove("Outcome")
assembler = VectorAssembler(inputCols=cols,outputCol="features")

data=assembler.transform(new_data)
# data.select("features",'Outcome').show(truncate=False)


train, tesT = df.randomSplit([0.7, 0.3])
x_col = new_data.columns
x_train = train.toPandas()[x_col[:-1]].values
y_train = train.toPandas()['Outcome'].values
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
cls = LogisticRegression()
cls.fit(x_train,y_train)

save_path = 'prediction/'
completeName = os.path.join(save_path, "dblogR.pkl")         
pickle.dump(cls, open(completeName, 'wb'))
