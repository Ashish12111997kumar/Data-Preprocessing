import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
data={"Index":[1,2,3,4,5,6,7,8,9,10],"Animal":["cat","dog","mouse","mouse","dog",'cat','lion','goat','cat','dog'],"gender":["MALE",'MALE','FEMALE','FEMALE','FEMALE','FEMALE','MALE','MALE','FEMALE','MALE'],"homly":["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes"],"types":["A","B","C","C","A","B","D","E","A","B"]}
catog=pd.DataFrame(data)
animal_dummy=pd.get_dummies(data["Animal"])#we can also drop first column using (drop_first= True)
gender_dummy=pd.get_dummies(data["gender"])
homly_dummy=pd.get_dummies(data["homly"])
types_dummy=pd.get_dummies(data["types"])
New_dataset=pd.concat([animal_dummy,gender_dummy,homly_dummy,types_dummy],axis=1)
print(New_dataset)
#############################



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
data={"Index":[1,2,3,4,5,6,7,8,9,10],"Animal":["cat","dog","mouse","mouse","dog",'cat','lion','goat','cat','dog'],"gender":["MALE",'MALE','FEMALE','FEMALE','FEMALE','FEMALE','MALE','MALE','FEMALE','MALE'],"homly":["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes"],"types":["A","B","C","C","A","B","D","E","A","B"]}
catog=pd.DataFrame(data)
one=preprocessing.OneHotEncoder(dtype=np.int64)
animalenc=pd.DataFrame(one.fit_transform(catog[["Animal"]]).toarray())
genderenc=pd.DataFrame(one.fit_transform(catog[["gender"]]).toarray())
homlyenc=pd.DataFrame(one.fit_transform(catog[["homly"]]).toarray())
typesenc=pd.DataFrame(one.fit_transform(catog[["types"]]).toarray())
Animal=animalenc.rename(columns={0:'Cat',1:"Dog",2:'goat',3:"lion",4:'mouse'})
Gender=genderenc.rename(columns={0:'female',1:"male"})
homly=homlyenc.rename(columns={0:'yes'})
types=typesenc.rename(columns={0:'A',1:"B",2:'C',3:"D",4:'E'})
new=pd.concat([Animal,Gender,homly,types],axis=1)
print(new)

################################



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
data={"Index":[1,2,3,4,5,6,7,8,9,10],"Animal":["cat","dog","mouse","mouse","dog",'cat','lion','goat','cat','dog'],"gender":["MALE",'MALE','FEMALE','FEMALE','FEMALE','FEMALE','MALE','MALE','FEMALE','MALE'],"homly":["yes","yes","yes","yes","yes","yes","yes","yes","yes","yes"],"types":["A","B","C","C","A","B","D","E","A","B"]}
catog=pd.DataFrame(data)
one=preprocessing.LabelEncoder()
catog["Animal"]=pd.DataFrame(one.fit_transform(catog[["Animal"]]))
catog["gender"]=pd.DataFrame(one.fit_transform(catog[["gender"]]))
catog["homly"]=pd.DataFrame(one.fit_transform(catog[["homly"]]))
catog["types"]=pd.DataFrame(one.fit_transform(catog[["types"]]))

print(catog)
