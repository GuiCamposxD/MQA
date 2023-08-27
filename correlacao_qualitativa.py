import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)

tabela_contigencia_1 = pd.crosstab(adult['Renda'], adult['Sexo'])
tabela_contigencia_2 = pd.crosstab(adult['Renda'], adult['Raça'])

chi2_1, p_1, dof_1, expected_1 = chi2_contingency(tabela_contigencia_1)
chi2_2, p_2, dof_2, expected_2 = chi2_contingency(tabela_contigencia_2)

p_valor = [p_1, p_2]

def calculate_percentage_frequencies(table):
    return (table / table.sum().sum()) * 100

percentage_table_1 = calculate_percentage_frequencies(tabela_contigencia_1)
percentage_table_2 = calculate_percentage_frequencies(tabela_contigencia_2)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

for i, (tabela_contigencia, title) in enumerate(
    zip(
        [percentage_table_1, percentage_table_2],
        ['Renda vs Sexo', 'Renda vs Raça'],
    )):
        tabela_contigencia.plot(kind='bar', ax=axes[i])
        axes[i].set_ylabel('Frequência')
        axes[i].set_title(f'{title}\n p-valor: {p_valor[i]:.5f}')
        axes[i].grid(axis='y')

plt.tight_layout()
plt.show()
