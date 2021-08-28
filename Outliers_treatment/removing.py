from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.stats import kurtosis
data=load_boston()
boston=pd.DataFrame(data.data,columns=data.feature_names)

def trimming(a,i):
  IQR=a.iloc[:,i].quantile(0.75)-a.iloc[:,i].quantile(0.25)
  Upper=a.iloc[:,i].quantile(0.75)+IQR*1.5
  Lower=a.iloc[:,i].quantile(0.25)-IQR*1.5
  df_out=np.where(a.iloc[:,i]>Upper,True,np.where(a.iloc[:,i]<Lower,True,False))
  trimmed=a.loc[~(df_out),]
  return trimmed




j=0
a=boston
while j!=7:
  i=0
  trimmed1=trimming(a,i)
  j+=1
  a=trimmed1
print(kurtosis(trimmed1.CRIM))


################################INDUS####################
j=0
a=trimmed1
while j!=0:
  i=2
  trimmed2=trimming(a,i)
  j+=1
  a=trimmed2
print(kurtosis(trimmed2.INDUS))

########################  ZN  ##############################
j=0
a=trimmed2
while j!=1:
  i=1
  trimmed3=trimming(a,i)
  j+=1
  a=trimmed3
print(kurtosis(trimmed3.ZN))

######################## IN CHAS, Most of the values are zero So this is not relevant column ##############################
j=0
a=trimmed3
while j!=3:
  i=3
  trimmed4=trimming(a,i)
  j+=1
  a=trimmed4
print(kurtosis(trimmed4.CHAS))
######################   NOX does not have outlier  #############################

################   RM   ######################
#['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
#       'PTRATIO', 'B', 'LSTAT']
#########################   RM   #####################
j=0
a=trimmed5
while j!=1:
  i=5
  trimmed6=trimming(a,i)
  j+=1
  a=trimmed6
print(kurtosis(trimmed6.RM))

################   AGE Column does not have outlier.   ###############################
plt.boxplot(trimmed6.AGE)
#######################  DIS  #########################
j=0
a=trimmed6
while j!=1:
  i=7
  trimmed7=trimming(a,i)
  j+=1
  a=trimmed7
print(kurtosis(trimmed7.DIS))
##################  RAD   ##############################
j=0
a=trimmed7
while j!=1:
  i=8
  trimmed8=trimming(a,i)
  j+=1
  a=trimmed8
print(kurtosis(trimmed8.RAD))

##############   TAX    ######################
j=0
a=trimmed8
while j!=1:
  i=9
  trimmed9=trimming(a,i)
  j+=1
  a=trimmed9
print(kurtosis(trimmed9.TAX))

############   PTRATIO   #####################
j=0
a=trimmed9
while j!=1:
  i=10
  trimmed10=trimming(a,i)
  j+=1
  a=trimmed10
print(kurtosis(trimmed10.PTRATIO))

##################   B    ####################
j=0
a=trimmed10
while j!=5:
  i=11
  trimmed11=trimming(a,i)
  j+=1
  a=trimmed11
print(kurtosis(trimmed11.B))
#plt.boxplot(trimmed11.B)

###############  LSTAT     ##################

j=0
a=trimmed11
while j!=5:
  i=12
  trimmed12=trimming(a,i)
  j+=1
  a=trimmed12
print(kurtosis(trimmed12.LSTAT))
plt.boxplot(trimmed12.LSTAT)
