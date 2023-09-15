import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

sns.set(style='whitegrid')
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
variaveis_quantitativas = [
    'Média das Notas no 1ºSemestre',
    'Média das Notas no 2ºSemestre',
    'GDP',
]

for i, variavel in enumerate(variaveis_quantitativas):
    sns.violinplot(
        data=data, 
        x='Prioridade Curso',
        y=variavel,
        palette='turbo',
        inner=None,
        linewidth=0,
        saturation=0.4,
        ax=axes[i],
    )
    sns.boxplot(
        data=data,
        x='Prioridade Curso',
        y=variavel,
        palette='turbo',
        width=0.3,
        boxprops={'zorder': 2},
        medianprops={'color': 'red'},
        ax=axes[i]
    )
    axes[i].set_xlabel('Prioridade Curso')
    axes[i].set_ylabel(variavel)
    axes[i].set_title(variavel + ' por Prioridade Curso')

plt.show()