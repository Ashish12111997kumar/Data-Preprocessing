from sklearn.datasets import load_boston
from feature_engine.outliers import Winsorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.stats import kurtosis
data=load_boston()
boston=pd.DataFrame(data.data,columns=data.feature_names)
def trimming(a):
  for i in range(13):
    IQR=a.iloc[:,i].quantile(0.75)-a.iloc[:,i].quantile(0.25)
    Upper=a.iloc[:,i].quantile(0.75)+IQR*1.5
    Lower=a.iloc[:,i].quantile(0.25)-IQR*1.5
    boston[i]=pd.DataFrame(np.where(a.iloc[:,i]>Upper,Upper,np.where(a.iloc[:,i]<Lower,Lower,a.iloc[:,i])))
  return boston

boston=trimming(boston)
replaced=boston.iloc[:,13:]
replaced=replaced.rename(columns={0:'CRIM',1:"ZN",2:'INDUS',3:"CHAS",4:'NOX',5:'RM',6:'AGE',7:'DIS',8:'RAD',9:'TAX',10:'PTRATIO',11:"B",12:'LSTAT'})
print(replaced)
