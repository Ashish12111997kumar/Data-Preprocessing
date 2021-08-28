from sklearn.datasets import load_boston
from feature_engine.outliers import Winsorizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.stats import kurtosis
data=load_boston()
boston=pd.DataFrame(data.data,columns=data.feature_names)
#plt.boxplot(boston.iloc[:,5])
for i in boston.columns:
  WS=Winsorizer(capping_method='iqr',fold=1.3,tail='both',variables=[i])
  boston[i]=pd.DataFrame(WS.fit_transform(boston[[i]]))

