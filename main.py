import pandas as pd
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'adult_bruto.xlsx'
path = os.path.join(pre, fname)

adult = pd.read_excel(path, na_values='?')

adult['occupation'].fillna(adult['occupation'].mode()[0], inplace=True)
adult['native-country'].fillna(adult['native-country'].mode()[0], inplace=True)

output_path = 'adult_bruto_alterado.xlsx'
adult.to_excel(output_path, index = False)

print(output_path)