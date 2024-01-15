import pandas as pd
import matplotlib.pyplot as plt

B = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# Reading a TXT file format
# H = pd.read_table('HR.txt')
# H.head()
# f=H['Department'].value_counts()