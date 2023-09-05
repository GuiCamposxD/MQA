import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(
    path,
    usecols=[
        'Idade na matrícula',
        'Nota de Admissão',
        'Média das Notas no 1ºSemestre',
        'Média das Notas no 2ºSemestre',
        'Taxa de desemprego',
        'GDP',
        'Sexo',
    ],
)

data['Sexo'] = data['Sexo'].map({'Feminino': 0, 'Masculino': 1})

matrix_correlacao = data.corr()
plt.figure(figsize=(5, 2))
sns.heatmap(matrix_correlacao, annot=True, cmap='Greys', vmin=-1, vmax=1, linewidth=.5)
plt.title('Matriz de Correlação')
plt.xticks(rotation=45)
plt.show()
