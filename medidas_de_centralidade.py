import pandas as pd
import os

file_path = 'adult.xlsx'
data = pd.read_excel(file_path)


media_idade = data['Idade'].mean()
media_anos_estudo = data['Anos de Estudo'].mean()
media_carga_horaria_semanal = data['Carga Horária Semanal'].mean()



moda_idade = data['Idade'].mode()
moda_anos_estudo = data['Anos de Estudo'].mode()
moda_carga_horaria_semanal = data['Carga Horária Semanal'].mode()




print('----------Idade------------')
print(f'Média: {media_idade}')
print(f'Moda: {moda_idade.iloc[0]}')
print()

print('----------Anos de Estudo------------')
print(f'Média: {media_anos_estudo}')
print(f'Moda: {moda_anos_estudo.iloc[0]}')
print()

print('----------Carga Horária Semanal-------------')
print(f'Média: {media_carga_horaria_semanal}')
print(f'Moda: {moda_carga_horaria_semanal.iloc[0]}')



