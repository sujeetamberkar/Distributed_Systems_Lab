import numpy as np
import pandas as pd

data = {"Name":["Sujeet","Abhishek","Manali"],"Height":[180,140,150],"Qualification":["B-tech","B-Tech","B-ed"]}
df = pd.DataFrame(data)
print(df)

address = ["Mumbai","Nagpur","Mumbai"]
df["Address"]=address

print(df)