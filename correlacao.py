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
        'Ganho de Capital',
        'Perca de Capital',
        'Carga Horária Semanal',
    ],
)

matrix_correlacao = adult.corr()
plt.figure(figsize=(5, 2))
sns.heatmap(matrix_correlacao, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidth=.5)
plt.title('Matriz de Correlação')
plt.show()
