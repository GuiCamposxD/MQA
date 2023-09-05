import pandas as pd
import os

file_path = 'adult.xlsx'
data = pd.read_excel(file_path)

contagem_valor = data['Etnia'].value_counts()
print(contagem_valor, '\n')

contagem_valor = data['Sexo'].value_counts()
print(contagem_valor, '\n')

contagem_valor = data['Renda'].value_counts()
print(contagem_valor, '\n')
