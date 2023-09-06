from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

variaveis = [
    'Nota de Admissão',
    'Idade na matrícula',
    'Média das Notas no 1ºSemestre',
    'Média das Notas no 2ºSemestre',
    'Taxa de desemprego',
    'GDP',
]

for i, variavel in enumerate(variaveis):
    media = np.mean(data[variavel])
    std = np.std(data[variavel], ddof=1)
    res = stats.kstest(data[variavel], cdf='norm', args=(media, std), N=len(data[variavel]))
    
    limite_critico = 1.36 / np.sqrt(len(data[variavel]))
    if res.statistic > limite_critico:
        print('Como a estatística do teste se mostrou um valor maior que o limite critíco, a variável não se mostra proveniente de uma distribuição normal')
        print()
    else:
        print('Como a estatística do teste se mostrou um valor menor que o limite critíco, a variável se mostra proveniente de uma distribuição normal')
        print()
