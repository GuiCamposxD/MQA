import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

variaveis = [
    "Idade na matrícula",
    "Média das Notas no 1ºSemestre",
    "Média das Notas no 2ºSemestre",
    "Taxa de desemprego",
    "Nota de Admissão",
    "GDP",
]


fig, axs = plt.subplots(3, 2, figsize=(12, 12)) 
plt.subplots_adjust(hspace=2)

for i, variavel in enumerate(variaveis):
    row = i // 2
    col = i % 2
    
    residuos = data[variavel]
    
    stats.probplot(residuos, dist="norm", plot=axs[row, col])

    axs[row, col].set_title(f'Probabilidade Normal - {variavel}')
    axs[row, col].set_xlabel("Quantis Teóricos")  # Rótulo do eixo X
    axs[row, col].set_ylabel("Resíduos")  # Rótulo do eixo Y
    
plt.tight_layout()
plt.show()