import pandas as pd
import numpy as np 

data = {'Age':[28,19,34,42], "Name":["Kavitha","Sudha","Raju","Vignesh"]}
df= pd.DataFrame(data,index=["rank1","rank2","rank3","rank4"])
print(df)
print(df.sort_values(by="Age"))