from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Binarizer
df=load_iris()
data=pd.DataFrame(df.data,columns=df.feature_names)
y=pd.DataFrame(df.target,columns=['type'])
iris=pd.concat([data,y],axis=1)
BN=Binarizer(iris.iloc[:,0].mean())
x=iris.iloc[:,0].values
x=x.reshape(1,-1)
iris['sepal length (cm)']=pd.DataFrame(BN.fit_transform(x).reshape(-1,1))
iris['sepal length (cm)']=iris['sepal length (cm)'].astype('int64')
############################
BN=Binarizer(iris.iloc[:,1].mean())
x=iris.iloc[:,1].values
x=x.reshape(1,-1)
iris['sepal width (cm)']=pd.DataFrame(BN.fit_transform(x).reshape(-1,1))
iris['sepal width (cm)']=iris['sepal width (cm)'].astype('int64')
##################################
BN=Binarizer(iris.iloc[:,2].mean())
x=iris.iloc[:,2].values
x=x.reshape(1,-1)
iris['petal length (cm)']=pd.DataFrame(BN.fit_transform(x).reshape(-1,1))
iris['petal length (cm)']=iris['petal length (cm)'].astype('int64')
######################################
BN=Binarizer(iris.iloc[:,3].mean())
x=iris.iloc[:,3].values
x=x.reshape(1,-1)
iris['petal width (cm)']=pd.DataFrame(BN.fit_transform(x).reshape(-1,1))
iris['petal width (cm)']=iris['petal width (cm)'].astype('int64')
print(iris)
