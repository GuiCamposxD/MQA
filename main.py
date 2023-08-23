import pandas as pd
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path, na_values='?')

adult['Ocupação'].fillna(adult['Ocupação'].mode()[0], inplace=True)
adult['País de Origem'].fillna(adult['País de Origem'].mode()[0], inplace=True)

output_path = 'adult_data_alterado.xlsx'
adult.to_excel(output_path, index = False)

print(output_path)