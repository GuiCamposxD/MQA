import pandas as pd
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path, na_values='?')

adult_filled = adult.fillna(adult.mode())

adult_filled['Classe de Trabalho'].fillna(adult_filled['Classe de Trabalho'].mode()[0], inplace=True)
adult_filled['País Nativo'].fillna(adult_filled['País Nativo'].mode()[0], inplace=True)

output_path = 'adult-data-alterado.xlsx'
adult_filled.to_excel(output_path, index = False)

print(output_path)