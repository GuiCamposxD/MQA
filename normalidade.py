import pandas as pd
from scipy.stats import kstest
from scipy.stats import norm
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)
amostra = adult['Idade']

# media_esperada = amostra.mean()
# desvio_padrao_esperado = amostra.std()
# resultado_teste = kstest(amostra, 'norm', args=(media_esperada, desvio_padrao_esperado))

# print('Média Esperada: ', media_esperada)
# print('Desvio Padrão: ', desvio_padrao_esperado)
# print('Resultado: ', resultado_teste)

# # valores_esperados = norm.rvs(loc=media_esperada, scale=desvio_padrao_esperado, size=len(amostra))

# # Criar um gráfico para visualizar os valores observados e esperados
# plt.figure(figsize=(10, 6))

# plt.hist(amostra, bins=20, density=True, alpha=0.5, label='Valores Observados')
# plt.hist(valores_esperados, bins=20, density=True, alpha=0.5, label='Valores Esperados')

# plt.xlabel('Valores')
# plt.ylabel('Frequência')
# plt.title('Comparação entre Valores Observados e Esperados')
# plt.legend()

# plt.show()

colunas_variaveis = ['Idade', 'Anos de Estudo', 'Ganho de Capital', 'Perca de Capital', 'Carga Horária Semanal']

num_linhas = 2
num_colunas =  3

fig, axes = plt.subplots(nrows=num_linhas, ncols=num_colunas, figsize=(12, 8))

for i, coluna in enumerate(colunas_variaveis):
    amostra = adult[coluna]
    
    media_amostra = amostra.mean()
    desvio_padrao_amostra = amostra.std()
    
    resultado_teste = kstest(amostra, 'norm', args=(media_amostra, desvio_padrao_amostra))
    valores_esperados = norm.rvs(loc=media_amostra, scale=desvio_padrao_amostra, size=len(amostra))

    row = i // num_colunas
    col = i % num_colunas
    ax = axes[row, col]

    ax.hist(amostra, bins=20, density=True, alpha=0.5, label='Valores Observados')
    ax.hist(valores_esperados, bins=20, density=True, alpha=0.5, label='Valores Esperados')

    ax.set_xlabel('Valores')
    ax.set_ylabel('Frequência')
    ax.set_title(f'Comparação para {coluna}')
    ax.legend()

plt.tight_layout()
plt.show()