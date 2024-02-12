import pandas as pd
import sys

# Assuming the first command line argument is the path to the Excel file
excel_file_path = sys.argv[1]

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Iterate over the DataFrame, outputting each value with a count of 1
for index, row in df.iterrows():
    for col in df.columns:
        value = row[col]
        print(f'{col}:{value}\t1')
