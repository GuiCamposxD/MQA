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
        'Carga Horária Semanal',
        'Renda',
        'Sexo',
    ],
)

adult['Renda'] = adult['Renda'].map({'<=50K': 0, '>50K': 1})
adult['Sexo'] = adult['Sexo'].map({'Feminino': 0, 'Masculino': 1})

matrix_correlacao = adult.corr()
plt.figure(figsize=(5, 2))
sns.heatmap(matrix_correlacao, annot=True, cmap='Greys', vmin=-1, vmax=1, linewidth=.5)
plt.title('Matriz de Correlação')
plt.xticks(rotation=45)
plt.show()
