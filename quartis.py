import pandas as pd
import os

file_path = 'adult.xlsx'
data = pd.read_excel(file_path)

primeiro_idade = data['Idade'].quantile(0.25)
primeiro_anos_estudo = data['Anos de Estudo'].quantile(0.25)
primeiro_carga_horaria_semanal = data['Carga Horária Semanal'].quantile(0.25)

mediana_idade = data['Idade'].median()
mediana_anos_estudo = data['Anos de Estudo'].median()
mediana_carga_horaria_semanal = data['Carga Horária Semanal'].median()

terceiro_idade = data['Idade'].quantile(0.75)
terceiro_anos_estudo = data['Anos de Estudo'].quantile(0.75)
terceiro_carga_horaria_semanal = data['Carga Horária Semanal'].quantile(0.75)

print('---------Idade-----------')
print(f'Primeiro Quartil: {primeiro_idade}')
print(f'Mediana: {mediana_idade}')
print(f'Terceiro Quartil {terceiro_idade}')
print()

print('---------Anos de estudo-----------')
print(f'Primeiro Quartil: {primeiro_anos_estudo}')
print(f'Mediana: {mediana_anos_estudo}')
print(f'Terceiro Quartil: {terceiro_anos_estudo}')
print()

print('---------Carga Horária Semanal-----------')
print(f'Primeiro Quartil: {primeiro_carga_horaria_semanal}')
print(f'Mediana: {mediana_carga_horaria_semanal}')
print(f'Terceiro Quartil {terceiro_carga_horaria_semanal}')
print()

print('Teste')


