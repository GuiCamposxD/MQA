import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(
    path,
    usecols=[
        'Idade',
        'Anos de Estudo',
        'Ganho de Investimento',
        'Perca de Investimento',
        'Carga Horária Semanal',
    ],
)

matrix_correlacao = adult.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(matrix_correlacao, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlação')
plt.show()
