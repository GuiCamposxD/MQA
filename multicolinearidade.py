import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)

variaveis_quantitativas = ['Idade', 'Anos de Estudo', 'Carga Horária Semanal']

adult_recortado = adult[variaveis_quantitativas]
adult_recortado_com_constante = add_constant(adult_recortado)

vif_data = pd.DataFrame()
vif_data["feature"] = adult_recortado_com_constante.columns
vif_data["VIF"] = [
    variance_inflation_factor(adult_recortado_com_constante.values, i) for i in range(adult_recortado_com_constante.shape[1])
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
