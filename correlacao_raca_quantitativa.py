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
        'Raça',
    ],
)

sns.set(style="whitegrid")
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

# sns.boxplot(x='Raça', y='Idade', data=adult, ax=axes[0])
# axes[0].set_xlabel("Raça")
# axes[0].set_ylabel("Idade")
# axes[0].set_title("Idade por Raça")

# sns.boxplot(x='Raça', y='Anos de Estudo', data=adult, ax=axes[1])
# axes[1].set_xlabel("Raça")
# axes[1].set_ylabel("Anos de Estudo")
# axes[1].set_title("Anos de Estudo por Raça")

sns.boxplot(x='Raça', y='Carga Horária Semanal', data=adult, ax=axes[2])
# axes[2].set_xlabel("Raça")
# axes[2].set_ylabel("Carga Horária Semanal")
# axes[2].set_title("Carga Horária Semanal por Raça")

plt.tight_layout()
plt.show()
