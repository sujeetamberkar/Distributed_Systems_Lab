import pandas as pd
import numpy as np

# Create a sample DataFrame
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Boolean Indexing: Fetch all rows where values in column 'A' are greater than 0
print("\nRows where column 'A' has positive values:")
print(df[df.A > 0])

# Add a new column 'F' with categorical data
# Make sure the list length matches the DataFrame's length
df['F'] = ['Male', 'Female', 'Female', 'Male', 'Female', 'Female']
print("\nDataFrame after adding column 'F':")
print(df)

# Setting values in column 'D' with a numpy array
# Replace the entire 'D' column with the value 5
df.loc[:, 'D'] = np.array([5] * len(df))
print("\nDataFrame after modifying column 'D' with 5s:")
print(df)


# Deleting a column 
df.drop('A',axis=1, inplace=True)
print(df)

# Deleting a row 
df.drop("20230101",axis=0,inplace=True)
print(df)



## Concat 

# Creating random data for two DataFrames
# DataFrame df1 with size 10x5
df1 = pd.DataFrame(np.random.rand(10, 5), columns=[f'Column_{i}' for i in range(1, 6)])

# DataFrame df2 with size 10x3
df2 = pd.DataFrame(np.random.rand(10, 3), columns=[f'Column_{i}' for i in range(6, 9)])

# Concatenating df1 and df2 horizontally
Df_new = pd.concat([df1, df2], axis=1)

# Displaying the first few rows of the new DataFrame and its shape
print(Df_new.head(), Df_new.shape)
