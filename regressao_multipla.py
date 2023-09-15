import pandas as pd
import statsmodels.api as sm
import os
import matplotlib.pyplot as plt

#caminho do arquivo
pre = os.path.dirname(os.path.realpath(__file__))
fname = 'Gastos-Academia.xlsx' #mudar o nome do arquivo
path = os.path.join(pre, fname)

# Carregar os dados do Excel em um DataFrame do Pandas
df = pd.read_excel(path)

# Definir as variáveis independentes (X) e a variável dependente (Y)
X = df[['horas', 'consumo']]  # variáveis independentes
Y = df['gastos']  #  variável dependente

# Adicionar uma constante para o termo de intercepto (β0)
X = sm.add_constant(X)

# Ajustar o modelo de regressão
modelo = sm.OLS(Y, X).fit()

#obtém os valores estimados
Y_estimado = modelo.predict(X)


# Imprimir o resumo estatístico do modelo
print(modelo.summary())

#plt.scatter(variavel eixo y, variável com valores reais ou valores estimados, cor, label da legenda)
plt.scatter(df['periodo'], Y, color='black', label='Valores Reais') #valores reais
plt.scatter(df['periodo'], Y_estimado, color='red', label='Valores Estimados') #valores estimados

plt.xlabel('Período') #variável de tempo
plt.ylabel('Gastos') #variável dependente
plt.title('Valores Reais vs. Valores Estimados')
plt.legend()
plt.show()





