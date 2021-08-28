# StandardScaler

import pandas as pd
from sklearn.preprocessing import StandardScaler
data=pd.read_csv('F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/Standardization and Normalization/Seeds_data.csv')
seed=data.iloc[:,-8:-1]
ss=StandardScaler()
df=ss.fit_transform(seed)
seed1=pd.DataFrame(df,columns=seed.columns)
print(seed1)
