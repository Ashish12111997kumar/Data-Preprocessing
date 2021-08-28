#We use tranformation techniques when we want our data to be normally distributed. 

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import math
data=pd.read_csv("F:/vrenv/Assignments/Data Preprocessing_Assignments/Solution/Transforamtion/calories_consumed.csv")
plt.hist(data['Weight gained (grams)']) # before tranformation visualized the shape of data distribution using Histogram on 'Weight gained (grams)' column
data['Weight gained (grams)'].skew()  # before transformation skewness is 1.2557366 on 'Weight gained (grams)' column.
data['Calories Consumed'].skew()   # before transformation skewness is 0.65492 on that is moderately acceptable.


# log technique
data['log_weight_gain']=np.log(data['Weight gained (grams)']).skew() # after transformation using log ,the skewness is 0.36064 it is symmetric. Best range of skewness is -0.5 to 0.5.
data['log_calories']=np.log(data['Calories Consumed']).skew() #    after transformation using log ,the skewness is 0.161982 it is symmetric.

# reciprocal technique

data['reci_calories']=1/data['Calories Consumed'].skew()  # so you can see reciprocal technique increased the skewness because tranformation techniques are hit andd trial techniques.
data['reci_weight']=1/data['Weight gained (grams)'].skew() # reciprocal technique did not work good on this feature also.

# sqrt technique

data['sqrt_calories']=data['Calories Consumed']**0.5 # improved but not that much.
data['sqrt_weight']=data['Weight gained (grams)']**0.5  # this also gave good skewness but log has given better than sqrt.

import scipy.stats as stat
import pylab

data['boxcox_calories'],box_calories=stat.boxcox(data['Calories Consumed'])
data['boxcox_weight'],box_weight=stat.boxcox(data['Weight gained (grams)'])
new_dataset=data.iloc[:,2:]
print(new_dataset) # I have concatinated all in one dataset just to make it easy for you to check it.
