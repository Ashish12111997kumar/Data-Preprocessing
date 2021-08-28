import pandas as pd
from sklearn.impute import SimpleImputer
import missingno as ms
import seaborn as sns
data=pd.read_csv("F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/missing values/claimants.csv")
# This dataset belongs to MAR.Because dataset features have weak correlation.
# Using PairWise deletion
def mean_(data1):
  si=SimpleImputer(missing_values=np.nan, strategy='mean')
  data1['CLMSEX']=pd.DataFrame(si.fit_transform(data1[['CLMSEX']]))
  data1['CLMINSUR']=pd.DataFrame(si.transform(data1[['CLMINSUR']]))
  data1['SEATBELT']=pd.DataFrame(si.transform(data1[['SEATBELT']]))
  data1['CLMAGE']=pd.DataFrame(si.transform(data1[['CLMAGE']]))
  return data1
data1=data
data_mean=mean_(data1)
print(data_mean)


def median_(data2):
  si=SimpleImputer(missing_values=np.nan, strategy='median')
  data2['CLMSEX']=pd.DataFrame(si.fit_transform(data2[['CLMSEX']]))
  data2['CLMINSUR']=pd.DataFrame(si.transform(data2[['CLMINSUR']]))
  data2['SEATBELT']=pd.DataFrame(si.transform(data2[['SEATBELT']]))
  data2['CLMAGE']=pd.DataFrame(si.transform(data2[['CLMAGE']]))
  return data2
data2=data
data_median=median_(data2)
print(data_median)


def mode_(data3):
  si=SimpleImputer(missing_values=np.nan, strategy='most_frequent')
  data3['CLMSEX']=pd.DataFrame(si.fit_transform(data3[['CLMSEX']]))
  data3['CLMINSUR']=pd.DataFrame(si.transform(data3[['CLMINSUR']]))
  data3['SEATBELT']=pd.DataFrame(si.transform(data3[['SEATBELT']]))
  data3['CLMAGE']=pd.DataFrame(si.transform(data3[['CLMAGE']]))
  return data3
data3=data
data_mode=mode_(data3)
print(data_mode)


def Constant_(data4):
  si=SimpleImputer(missing_values=np.nan, strategy='constant')
  data4['CLMSEX']=pd.DataFrame(si.fit_transform(data4[['CLMSEX']]))
  data4['CLMINSUR']=pd.DataFrame(si.transform(data4[['CLMINSUR']]))
  data4['SEATBELT']=pd.DataFrame(si.transform(data4[['SEATBELT']]))
  data4['CLMAGE']=pd.DataFrame(si.transform(data4[['CLMAGE']]))
  return data4
data4=data
data_constant=Constant_(data4)
print(data_constant)


