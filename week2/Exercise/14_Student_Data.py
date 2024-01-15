import numpy as np
import pandas as pd

data = {"Name":["Sujeet","Abhishek","Manali"],"Height":[180,140,150],"Qualification":["B-tech","B-Tech","B-ed"]}
df = pd.DataFrame(data)
address = ["Mumbai","Nagpur","Mumbai"]

df.insert(column="Adress", value= address, loc=3)
print(df)