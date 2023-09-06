import pandas as pd
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

contagem_valor = data['Curso'].value_counts()
print(contagem_valor, '\n')

contagem_valor = data['Ocupação Materna'].value_counts()
print(contagem_valor, '\n')

contagem_valor = data['Ocupação Paterna'].value_counts()
print(contagem_valor, '\n')

contagem_valor = data['Sexo'].value_counts()
print(contagem_valor, '\n')

contagem_valor = data['Situação Da Graduação'].value_counts()
print(contagem_valor, '\n')


