import pandas as pd
data={"Name":["Annie","Diya","Charles","James","Emily"],"Quiz_1/10":[8.0,9.0,7.5,8.5,6.5],"In-Sem_1/15":[11,14,14.5,13,12.5],"Quiz_2/10":[9.5,6.5,8.5,9.0,9.0],"In-Sem_2/15":[12.5,13.5,14.5,15.0,13.0]}
df = pd.DataFrame(data)
print(df)

df["Total"] = df[["Quiz_1/10","In-Sem_1/15","Quiz_2/10","In-Sem_2/15"]].sum(axis=1)
# Adding the mean row properly
df.loc['Mean'] = df.mean()
print(df)