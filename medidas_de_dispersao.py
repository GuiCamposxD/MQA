import pandas as pd
import os

file_path = 'adult.xlsx'
data = pd.read_excel(file_path)

variancia_idade = data['Idade'].var()
variancia_anos_estudo = data['Anos de Estudo'].var()
variancia_carga_horaria_semanal = data['Carga Horária Semanal'].var()

desvio_padrao_idade = data['Idade'].std()
desvio_padrao_anos_estudo = data['Anos de Estudo'].std()
desvio_padrao_carga_horaria_semanal = data['Carga Horária Semanal'].std()

media_idade = data['Idade'].mean()
media_anos_estudo = data['Anos de Estudo'].mean()
media_carga_horaria_semanal = data['Carga Horária Semanal'].mean()

coeficiente_variacao_idade = (desvio_padrao_idade/media_idade) * 100
coeficiente_variacao_anos_estudo = (desvio_padrao_anos_estudo/media_anos_estudo) * 100
coeficiente_variacao_carga_horaria_semanal = (desvio_padrao_carga_horaria_semanal/media_carga_horaria_semanal) * 100



print('---------Idade-----------')
print(f'Variância: {variancia_idade}')
print(f'Desvio Padrão: {desvio_padrao_idade}')
print(f'Coeficiente de Variação: {coeficiente_variacao_idade}')
print()

print('---------Anos de Estudo-----------')
print(f'Variância: {variancia_anos_estudo}')
print(f'Desvio Padrão: {desvio_padrao_anos_estudo}')
print(f'Coeficiente de Variação: {coeficiente_variacao_anos_estudo}')
print()

print('---------Carga Horária Semanal-----------')
print(f'Variância: {variancia_carga_horaria_semanal}')
print(f'Desvio Padrão: {desvio_padrao_carga_horaria_semanal}')
print(f'Coeficiente de Variação: {coeficiente_variacao_carga_horaria_semanal}')
print()





