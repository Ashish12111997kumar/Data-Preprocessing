import pandas as pd
from sklearn.impute import SimpleImputer
import missingno as ms
import seaborn as sns
data=pd.read_csv("F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/missing values/claimants.csv")

# List wise

data5=data
data5=data5.dropna()
print(data5)

# dropping columns
data6=data
data6=data6.drop(['CLMAGE','SEATBELT','CLMINSUR'],axis=1)
print(data6)
