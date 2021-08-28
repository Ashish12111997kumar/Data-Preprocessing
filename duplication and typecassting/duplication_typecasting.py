import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
df=pd.read_csv("F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/duplication and typecassting/OnlineRetail.csv", encoding= 'unicode_escape')
df["CustomerID"].fillna(df["CustomerID"].mean(),inplace=True)
df["UnitPrice"]=df["UnitPrice"].astype('int64')
df["CustomerID"]=df["CustomerID"].astype('int64')
print(df.duplicated().sum());print(df.duplicated())
df.drop_duplicates(inplace=True)
print("mean of quantity",df["Quantity"].mean())
print("skewness of quantity",df["Quantity"].skew())
print("skewness of UnitPrice",df["UnitPrice"].skew())
print("mean of Unit Price",df["UnitPrice"].mean())
print("median of quantity",df["Quantity"].median())
print("median of UnitPrice",df["UnitPrice"].median())
print("mode of quantity",df["Quantity"].mode())
print("mode of UnitPrice",df["UnitPrice"].mode())
print("variance of UnitPrice ",statistics.variance(df["UnitPrice"]))
print("variance of Quantity",statistics.variance(df["Quantity"]))
print("SD of Quantity",np.std(df["Quantity"]))
print("SD of UnitPrice",np.std(df["UnitPrice"]))
print("kurtosis of Quanity",kurtosis(df["Quantity"]))
print("kurtosis of UnitPrice",kurtosis(df["UnitPrice"]))
plt.boxplot(df["Quantity"])
plt.boxplot(df["UnitPrice"])
plt.hist(df["Quantity"])
plt.hist(df["UnitPrice"])
plt.hist(df["UnitPrice"])
plt.scatter(df["UnitPrice"],df["Quantity"])
plt.xlabel("Unit Price")
plt.ylabel("Quantity")
plt.show()