from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
from scipy.stats import johnsonsu

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)



def min_max_normalization(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

def z_score_normalization(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean) / std_dev
    return normalized_data



amostra_normalizada_z_score = z_score_normalization(data['Nota de Admissão'])
amostra_normalizada_min_max = min_max_normalization(data['Nota de Admissão'])
amostra_normalizada_log = np.log(data['Nota de Admissão'])
amostra_normalizada_raiz = np.sqrt(data['Nota de Admissão'])
#Normalização de Johnson
parametros_johnson = johnsonsu.fit(data['Nota de Admissão'])
amostra_normalizada_johnson= johnsonsu(*parametros_johnson).ppf(johnsonsu.cdf(data['Nota de Admissão'], *parametros_johnson))

#distribuição entre grupos 
valor_qualitativo_desejado = 'Matriculado'
registros_filtrados_matriculados = data[data['Situação Da Graduação'] == valor_qualitativo_desejado]
nota_de_admissao_matriculados = registros_filtrados_matriculados['Nota de Admissão']

valor_qualitativo_desejado = 'Desistente'
registros_filtrados_desistentes = data[data['Situação Da Graduação'] == valor_qualitativo_desejado]
nota_de_admissao_desistentes = registros_filtrados_desistentes['Nota de Admissão']

valor_qualitativo_desejado = 'Diplomado'
registros_filtrados_diplomado = data[data['Situação Da Graduação'] == valor_qualitativo_desejado]
nota_de_admissao_diplomado = registros_filtrados_diplomado['Nota de Admissão']


#normalizações entre grupos

diplomados_amostra_normalizada_z_score = z_score_normalization(nota_de_admissao_diplomado)
diplomados_amostra_normalizada_min_max = min_max_normalization(nota_de_admissao_diplomado)
diplomados_amostra_normalizada_log = np.log(nota_de_admissao_diplomado)
diplomados_amostra_normalizada_raiz = np.sqrt(nota_de_admissao_diplomado)
#Normalização de Johnson
diplomados_parametros_johnson = johnsonsu.fit(nota_de_admissao_diplomado)
diplomados_amostra_normalizada_johnson= johnsonsu(*diplomados_parametros_johnson).ppf(johnsonsu.cdf(nota_de_admissao_diplomado, *diplomados_parametros_johnson))


matriculados_amostra_normalizada_z_score = z_score_normalization(nota_de_admissao_matriculados)
matriculados_amostra_normalizada_min_max = min_max_normalization(nota_de_admissao_matriculados)
matriculados_amostra_normalizada_log = np.log(nota_de_admissao_matriculados)
matriculados_amostra_normalizada_raiz = np.sqrt(nota_de_admissao_matriculados)
#Normalização de Johnson
matriculados_parametros_johnson = johnsonsu.fit(nota_de_admissao_matriculados)
matriculados_amostra_normalizada_johnson= johnsonsu(*matriculados_parametros_johnson).ppf(johnsonsu.cdf(nota_de_admissao_matriculados, *parametros_johnson))


#testes de normalidade

ks_statistic_min_max, ks_p_value_min_max = stats.kstest(amostra_normalizada_min_max, 'norm')
ks_statistic_z, ks_p_value_z = stats.kstest(amostra_normalizada_z_score, 'norm')
ks_statistic_log, ks_p_value_log = stats.kstest(amostra_normalizada_log, 'norm')
ks_statistic_raiz, ks_p_value_raiz = stats.kstest(amostra_normalizada_raiz, 'norm')
ks_statistic_johnson, ks_p_value_johnson = stats.kstest(amostra_normalizada_johnson, 'norm')

ks_statistic_nota_admissao_matriculados, ks_p_value_nota_admissao_matriculados = stats.kstest(nota_de_admissao_matriculados, 'norm')

ks_statistic_nota_admissao_diplomados_normalizada, ks_p_value_nota_admissao_diplomados_normalizada = stats.kstest(diplomados_amostra_normalizada_johnson, 'norm')

ks_statistic_nota_admissao_matriculados_normalizada, ks_p_value_nota_admissao_matriculados_normalizada = stats.kstest(matriculados_amostra_normalizada_johnson, 'norm')








stats_shap_min_max, p_value_shap_min_max = stats.shapiro(amostra_normalizada_min_max)
stats_shap_z, p_value_shap_z = stats.shapiro(amostra_normalizada_z_score)
stats_shap_log, p_value_shap_log = stats.shapiro(amostra_normalizada_log)
stats_shap_raiz, p_value_shap_raiz = stats.shapiro(amostra_normalizada_raiz)
stats_shap_johnson, p_value_shap_johnson = stats.shapiro(amostra_normalizada_johnson)
p_value_shap_nota_admissao_matriculados = stats.shapiro(amostra_normalizada_johnson)
nada, p_value_shap_nota_admissao_diplomados_normalizada = stats.shapiro(diplomados_amostra_normalizada_johnson)
nada, p_value_shap_nota_admissao_matriculados_normalizada = stats.shapiro(matriculados_amostra_normalizada_johnson)









# print(ks_p_value_min_max)
# print(p_value_shap_min_max)



# print(p_value_shap_z)
# print(ks_p_value_z)

# print(p_value_shap_log)
# print(ks_p_value_log)

# print(p_value_shap_raiz)
# print(ks_p_value_raiz)

# print(p_value_shap_johnson)
# print(ks_p_value_johnson)

# print(ks_p_value_nota_admissao_matriculados)
# print(p_value_shap_nota_admissao_matriculados)

# print(ks_p_value_nota_admissao_diplomados_normalizada)
# print(p_value_shap_nota_admissao_diplomados_normalizada)

print(ks_p_value_nota_admissao_matriculados_normalizada)
print(p_value_shap_nota_admissao_matriculados_normalizada)

plt.figure(figsize=(10, 6))
sns.histplot(matriculados_amostra_normalizada_johnson, kde=True, color='blue', bins=20)  # Use kde=False para ocultar o KDE
plt.title('Histograma com KDE')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()



