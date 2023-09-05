import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

variaveis = [
    'Idade na matrícula',
    'Nota de Admissão',
    'Média das Notas no 1ºSemestre',
    'Média das Notas no 2ºSemestre',
    'Taxa de desemprego',
    'GDP',
]

data_recortado = data[variaveis]

vif_data = pd.DataFrame()
vif_data["feature"] = data_recortado.columns
vif_data["VIF"] = [
    variance_inflation_factor(data_recortado.values, i) for i in range(data_recortado.shape[1])
]

print(vif_data)

plt.figure(figsize=(10, 6))
bars = plt.barh(vif_data["feature"], vif_data["VIF"], color='skyblue')
plt.xlabel('VIF Value')
plt.ylabel('Variáveis')
plt.title('Valores do VIF')
plt.gca().invert_yaxis()
for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}', 
             va='center', ha='left', color='black', fontsize=10)

plt.show()
