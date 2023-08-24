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
        'Renda',
    ],
)

sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=1, ncols=5, figsize=(18, 6))

# Criar os box plots
sns.boxplot(x='Renda', y='Idade', data=adult, ax=axes[0])
axes[0].set_xlabel("Renda")
axes[0].set_ylabel("Idade")
axes[0].set_title("Idade por Renda")

sns.boxplot(x='Renda', y='Anos de Estudo', data=adult, ax=axes[1])
axes[1].set_xlabel("Renda")
axes[1].set_ylabel("Anos de Estudo")
axes[1].set_title("Anos de Estudo por Renda")

sns.boxplot(x='Renda', y='Ganho de Investimento', data=adult, ax=axes[2])
axes[2].set_xlabel("Renda")
axes[2].set_ylabel("Ganho de Investimento")
axes[2].set_title("Anos de Educação por Renda")

sns.boxplot(x='Renda', y='Perca de Investimento', data=adult, ax=axes[3])
axes[3].set_xlabel("Renda")
axes[3].set_ylabel("Perca de Investimento")
axes[3].set_title("Perca de Investimento por Renda")

sns.boxplot(x='Renda', y='Carga Horária Semanal', data=adult, ax=axes[4])
axes[4].set_xlabel("Renda")
axes[4].set_ylabel("Carga Horária Semanal")
axes[4].set_title("Carga Horária Semanal por Renda")

plt.tight_layout()  # Ajusta o layout dos subplots
plt.show()  # Mostrar o gráfico
