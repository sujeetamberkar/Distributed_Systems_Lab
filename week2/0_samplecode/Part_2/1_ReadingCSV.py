import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('xyz.csv',header=None)
print(df.head()) # Head 
print(df.tail()) # Tail

df.columns = ["Preg","glu","bp","sft","ins","bmi","dpf","age","class"]
plt.scatter(df['bmi'],df['glu'])

plt.xlabel('bmi')
plt.ylabel('Glucose')

# plt.show()

df['age'].hist()
plt.show()
