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

colunas_variaveis = ['Idade', 'Anos de Estudo', 'Carga Horária Semanal']

num_linhas = 1
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