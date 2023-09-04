from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path)

variable_name = 'Idade'
sample_data = adult[variable_name]

ks_statistic, ks_p_value = stats.kstest(sample_data, 'norm')

print("Teste de Kolmogorov-Smirnov para", variable_name)
print("Estatística de teste:", ks_statistic)
print("Valor p:", ks_p_value)

plt.figure(figsize=(10, 6))
plt.hist(sample_data, bins=20, density=True, alpha=0.6, color='blue', label='Dados de amostra')
plt.xlabel(variable_name)
plt.ylabel('Densidade')
plt.title('Histograma e Distribuição Teórica')
plt.legend()

x = np.linspace(sample_data.min(), sample_data.max(), 100)
plt.plot(x, stats.norm.pdf(x, loc=sample_data.mean(), scale=sample_data.std()), color='red', label='Distribuição normal')
plt.legend()

plt.grid()
plt.show()
