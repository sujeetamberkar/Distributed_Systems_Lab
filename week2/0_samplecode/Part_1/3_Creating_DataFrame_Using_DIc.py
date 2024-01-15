import pandas as pd
import numpy as np
df = pd.DataFrame({'A':pd.Timestamp(20130102),'B':np.array([3]*4,dtype='int32'), 'C':pd.Categorical(['Male','Female','Male','Female'])})
print(df)

print("\nShape")

print(df.shape)
print("\ndtypes")
print(df.dtypes)


print("\nPrint Head: first 5 ")
print(df.head())

print("\nPrint Tail: last 5 ")
print(df.tail())

print("\nInfo")
print(df.info())


print("\nDescribe")
print(df.describe())


print("Transpose")
print(df.T)