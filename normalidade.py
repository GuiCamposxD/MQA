from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

variaveis = [
    'Nota de Admissão',
    'Idade na matrícula',
    'Média das Notas no 1ºSemestre',
    'Média das Notas no 2ºSemestre',
    'Taxa de desemprego',
    'GDP',
]

fig, axs = plt.subplots(3, 2, figsize=(12, 10))
fig.subplots_adjust(hspace=0.5)

for i, variavel in enumerate(variaveis):
    dados = data[variavel].dropna()
    
    ks_stat, p_value = stats.kstest(dados, 'norm', (dados.mean(), dados.std()))
    
    axs[i // 2, i % 2].hist(dados, bins=30, density=True, alpha=0.6, color='b', label='Dados')
    
    xmin, xmax = min(dados), max(dados)
    x = np.linspace(xmin, xmax, 100)
    y = stats.norm.pdf(x, dados.mean(), dados.std())
    axs[i // 2, i % 2].plot(x, y, 'r--', label='Distribuição Normal')
    
    axs[i // 2, i % 2].set_title(f'Teste KS para {variavel}\nKS p-value: {p_value:.4f}')
    axs[i // 2, i % 2].legend()

plt.tight_layout()
plt.show()