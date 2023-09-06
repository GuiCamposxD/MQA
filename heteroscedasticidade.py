import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

variaveis_independentes = [
    "Média das Notas no 1ºSemestre",
    "Idade na matrícula",
    "Média das Notas no 2ºSemestre",
    "Taxa de desemprego",
    "GDP",
]

data["intercept"] = 1

X = data[['intercept'] + variaveis_independentes]
y = data["Nota de Admissão"]

modelo = sm.OLS(y, X)
resultado = modelo.fit()

residuos = resultado.resid
resultado_teste = het_white(residuos, exog=X)

print("Estatística do teste White:", resultado_teste[0])
print("Valor-p do teste White:", resultado_teste[1])

alpha = 0.05
if resultado_teste[1] < alpha:
    print("Rejeitar a hipótese nula: Heterocedasticidade está presente.")
else:
    print("Não rejeitar a hipótese nula: Não há evidência de heterocedasticidade.")