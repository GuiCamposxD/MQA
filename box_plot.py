import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)

sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

sns.boxplot(
    x='Renda',
    y='Idade',
    hue="Sexo",
    data=adult,
    ax=axes[0],
    palette="Set3",
    medianprops={'color': 'red'},
)
print(adult.groupby(["Renda", "Sexo"])["Idade"].describe())
axes[0].set_xlabel("Renda")
axes[0].set_ylabel("Idade")
axes[0].set_title("Idade por Renda Condicionado em Sexo")

sns.boxplot(
    x='Renda',
    y='Anos de Estudo',
    hue="Sexo",
    data=adult,
    ax=axes[1],
    palette="Set3",
    medianprops={'color': 'red'},
)
print(adult.groupby(["Renda", "Sexo"])["Anos de Estudo"].describe())
axes[1].set_xlabel("Renda")
axes[1].set_ylabel("Anos de Estudo")
axes[1].set_title("Anos de Estudo por Renda Condicionado em Sexo")

sns.boxplot(
    x='Renda',
    y='Carga Horária Semanal',
    hue="Sexo",
    data=adult,
    ax=axes[2],
    palette="Set3",
    medianprops={'color': 'red'},
)
print(adult.groupby(["Renda", "Sexo"])["Carga Horária Semanal"].describe())
axes[2].set_xlabel("Renda")
axes[2].set_ylabel("Carga Horária Semanal")
axes[2].set_title("Carga Horária Semanal por Renda Condicionado em Sexo")

plt.tight_layout()
plt.show()
