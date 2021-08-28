# Normalization or MinMaxScaler

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data1=pd.read_csv('F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/Standardization and Normalization/Seeds_data.csv')
seed2=data1.iloc[:,-8:-1]
MS=MinMaxScaler()
df1=MS.fit_transform(seed2)
seed3=pd.DataFrame(df1,columns=seed2.columns)
print(seed3)
