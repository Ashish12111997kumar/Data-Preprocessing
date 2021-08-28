from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv('F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/zero variance/Z_dataset.csv')
LE=LabelEncoder()
data['colour']=LE.fit_transform(data['colour'])
VT=VarianceThreshold(threshold=0.25999999999999998)
New=pd.DataFrame(VT.fit_transform(data).astype('int'),columns=data.columns[0:5])
print(New)
