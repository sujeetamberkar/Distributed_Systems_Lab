import pandas as pd
data = pd.read_excel('German.xlsx')
# print(data.head())
lista = data['DurationOfCreditInMonths'].tolist()
# print(lista)

for i in lista:
    print(i,end=" ")