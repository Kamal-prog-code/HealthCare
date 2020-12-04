import pandas as pd
import matplotlib.pyplot as plt
import pylab
from pandas import DataFrame
import statistics
import scipy.stats
import os

from sklearn.model_selection import train_test_split

df=pd.read_csv('media/diab.csv')
print(df)
features=df.keys().to_list()
print(features[:-1])
X = df[features[:-1]]
y=df.Outcome
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,shuffle=True)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import pickle
k=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
Accuracy={}

for i in k:
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    Accuracy[i]=metrics.accuracy_score(y_test, pred)
model1=KNeighborsClassifier(n_neighbors=12)
model1.fit(X_train,y_train)
plt.plot(*zip(*sorted(Accuracy.items())))
plt.title("Choose value of k")
plt.xlabel("k")
plt.ylabel("Accuracy")
# plt.show()
save_path = 'prediction/'
completeName = os.path.join(save_path, "knn.pkl")         
pickle.dump(model1, open(completeName, 'wb'))

