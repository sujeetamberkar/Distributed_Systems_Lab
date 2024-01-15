import pandas as pd
import numpy as np 
dates=pd.date_range('20130101', periods=100)
df = pd.DataFrame(np.random.randn(100,4),index=dates, columns=list('ABCD'))

print("First 5")
print(df.head())

print("Last 5")
print(df.tail())

print("\nIndex")
print(df.index)


print("\nColumns")
print(df.columns)


print("\nTranspose")
print(df.T)

print("\nSorting by Axis")
print(df.sort_index(axis=1, ascending=False))


print("\nSorting by Values")
print(df.sort_values(by="B"))

print("\nSlicing the rows")
print(df[0:3])


print("\nSlicing WIth Index Name")
print(df["20130105":"20130110"])


print("\n Slicing Rows and Column")
print(df.iloc[0]) # will fetch entire 1 st row
print(df.iloc[0,:2]) # Will fetch first row (Column 1 and 2)
print(df.iloc[0,0]) # will fetch first row, first column (Single element)

print(df['A']) # Selecting Column "A"
# print("Sujeet")
print(df[['A','B']]) # Entire column "A" and "B"



print(df[['A','B']][:5]) #column "A" and "B" but only first 5 rows
print(df.loc['20130101':'20130105',['A','B']][:5])