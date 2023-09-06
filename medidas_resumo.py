import pandas as pd
import os

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'data.xlsx'
path = os.path.join(pre, fname)

data = pd.read_excel(path)

#variâncias
variancia_prioridade_curso = data['Prioridade Curso'].var()
variancia_nota_admissao = data['Nota de Admissão'].var()
variancia_idade_matricula = data['Idade na matrícula'].var()
variancia_media_notas_1sem = data['Média das Notas no 1ºSemestre'].var()
variancia_media_notas_2sem = data['Média das Notas no 2ºSemestre'].var()
variancia_taxa_desemprego = data['Taxa de desemprego'].var()
variancia_gdp = data['GDP'].var()

#desvios padrões
desvio_padrao_prioridade_curso = data['Prioridade Curso'].std()
desvio_padrao_nota_admissao = data['Nota de Admissão'].std()
desvio_padrao_idade_matricula = data['Idade na matrícula'].std()
desvio_padrao_media_notas_1sem = data['Média das Notas no 1ºSemestre'].std()
desvio_padrao_media_notas_2sem = data['Média das Notas no 2ºSemestre'].std()
desvio_padrao_taxa_desemprego = data['Taxa de desemprego'].std()
desvio_padrao_gdp = data['GDP'].std()

#médias
media_prioridade_curso = data['Prioridade Curso'].mean()
media_nota_admissao = data['Nota de Admissão'].mean()
media_idade_matricula = data['Idade na matrícula'].mean()
media_media_notas_1sem = data['Média das Notas no 1ºSemestre'].mean()
media_media_notas_2sem = data['Média das Notas no 2ºSemestre'].mean()
media_taxa_desemprego = data['Taxa de desemprego'].mean()
media_gdp = data['GDP'].mean()

#coeficientes de variação
coeficiente_variacao_prioridade_curso = (desvio_padrao_prioridade_curso/media_prioridade_curso) * 100
coeficiente_variacao_nota_admissao = (desvio_padrao_nota_admissao/media_nota_admissao) * 100
coeficiente_variacao_idade_matricula = (desvio_padrao_idade_matricula/media_idade_matricula) * 100
coeficiente_variacao_media_notas_1sem = (desvio_padrao_media_notas_1sem/media_media_notas_1sem) * 100
coeficiente_variacao_media_notas_2sem = (desvio_padrao_media_notas_2sem/media_media_notas_2sem) * 100
coeficiente_variacao_taxa_desemprego = (desvio_padrao_taxa_desemprego/media_taxa_desemprego) * 100
coeficiente_variacao_gdp = (desvio_padrao_gdp/media_gdp) * 100


#modas
moda_prioridade_curso = data['Prioridade Curso'].mode()
moda_nota_admissao = data['Nota de Admissão'].mode()
moda_idade_matricula = data['Idade na matrícula'].mode()
moda_media_notas_1sem = data['Média das Notas no 1ºSemestre'].mode()
moda_media_notas_2sem = data['Média das Notas no 2ºSemestre'].mode()
moda_taxa_desemprego = data['Taxa de desemprego'].mode()
moda_gdp = data['GDP'].mode()


#primeiros quartis
primeiro_quartil_prioridade_curso = data['Prioridade Curso'].quantile(0.25)
primeiro_quartil_nota_admissao = data['Nota de Admissão'].quantile(0.25)
primeiro_quartil_idade_matricula = data['Idade na matrícula'].quantile(0.25)
primeiro_quartil_media_notas_1sem = data['Média das Notas no 1ºSemestre'].quantile(0.25)
primeiro_quartil_media_notas_2sem = data['Média das Notas no 2ºSemestre'].quantile(0.25)
primeiro_quartil_taxa_desemprego = data['Taxa de desemprego'].quantile(0.25)
primeiro_quartil_gdp = data['GDP'].quantile(0.25)

#segundos quartis
segundo_quartil_prioridade_curso = data['Prioridade Curso'].quantile(0.5)
segundo_quartil_nota_admissao = data['Nota de Admissão'].quantile(0.5)
segundo_quartil_idade_matricula = data['Idade na matrícula'].quantile(0.5)
segundo_quartil_media_notas_1sem = data['Média das Notas no 1ºSemestre'].quantile(0.5)
segundo_quartil_media_notas_2sem = data['Média das Notas no 2ºSemestre'].quantile(0.5)
segundo_quartil_taxa_desemprego = data['Taxa de desemprego'].quantile(0.5)
segundo_quartil_gdp = data['GDP'].quantile(0.5)

#terceiros quartis
terceiro_quartil_prioridade_curso = data['Prioridade Curso'].quantile(0.75)
terceiro_quartil_nota_admissao = data['Nota de Admissão'].quantile(0.75)
terceiro_quartil_idade_matricula = data['Idade na matrícula'].quantile(0.75)
terceiro_quartil_media_notas_1sem = data['Média das Notas no 1ºSemestre'].quantile(0.75)
terceiro_quartil_media_notas_2sem = data['Média das Notas no 2ºSemestre'].quantile(0.75)
terceiro_quartil_taxa_desemprego = data['Taxa de desemprego'].quantile(0.75)
terceiro_quartil_gdp = data['GDP'].quantile(0.75)







print('---------Prioridade Curso-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_prioridade_curso}')
print(f'Moda: {moda_prioridade_curso.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_prioridade_curso}')
print(f'Desvio Padrão: {desvio_padrao_prioridade_curso}')
print(f'Coeficiente de Variação: {coeficiente_variacao_prioridade_curso}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_prioridade_curso}')
print(f'Segundo Quartil: {segundo_quartil_prioridade_curso}')
print(f'Terceiro Quartil: {terceiro_quartil_prioridade_curso}')
print()

print('---------Nota de Admissão-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_nota_admissao}')
print(f'Moda: {moda_nota_admissao.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_nota_admissao}')
print(f'Desvio Padrão: {desvio_padrao_nota_admissao}')
print(f'Coeficiente de Variação: {coeficiente_variacao_nota_admissao}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_nota_admissao}')
print(f'Segundo Quartil: {segundo_quartil_nota_admissao}')
print(f'Terceiro Quartil: {terceiro_quartil_nota_admissao}')
print()

print('---------Idade na matrícula-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_idade_matricula}')
print(f'Moda: {moda_idade_matricula.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_idade_matricula}')
print(f'Desvio Padrão: {desvio_padrao_idade_matricula}')
print(f'Coeficiente de Variação: {coeficiente_variacao_idade_matricula}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_idade_matricula}')
print(f'Segundo Quartil: {segundo_quartil_idade_matricula}')
print(f'Terceiro Quartil: {terceiro_quartil_idade_matricula}')
print()

print('---------Média das Notas no 1ºSemestre-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_media_notas_1sem}')
print(f'Moda: {moda_media_notas_1sem.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_media_notas_1sem}')
print(f'Desvio Padrão: {desvio_padrao_media_notas_1sem}')
print(f'Coeficiente de Variação: {coeficiente_variacao_media_notas_1sem}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_media_notas_1sem}')
print(f'Segundo Quartil: {segundo_quartil_media_notas_1sem}')
print(f'Terceiro Quartil: {terceiro_quartil_media_notas_1sem}')
print()

print('---------Média das Notas no 2ºSemestre-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_media_notas_2sem}')
print(f'Moda: {moda_media_notas_2sem.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_media_notas_2sem}')
print(f'Desvio Padrão: {desvio_padrao_media_notas_2sem}')
print(f'Coeficiente de Variação: {coeficiente_variacao_media_notas_2sem}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_media_notas_2sem}')
print(f'Segundo Quartil: {segundo_quartil_media_notas_2sem}')
print(f'Terceiro Quartil: {terceiro_quartil_media_notas_2sem}')

print()

print('---------Taxa de desemprego-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_taxa_desemprego}')
print(f'Moda: {moda_taxa_desemprego.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_taxa_desemprego}')
print(f'Desvio Padrão: {desvio_padrao_taxa_desemprego}')
print(f'Coeficiente de Variação: {coeficiente_variacao_taxa_desemprego}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_taxa_desemprego}')
print(f'Segundo Quartil: {segundo_quartil_taxa_desemprego}')
print(f'Terceiro Quartil: {terceiro_quartil_taxa_desemprego}')

print()

print('---------GDP-----------')

print('Medidas de Centralidade: ')
print(f'Média: {media_gdp}')
print(f'Moda: {moda_gdp.iloc[0]}')

print('Medidas de dispersão: ')
print(f'Variância: {variancia_gdp}')
print(f'Desvio Padrão: {desvio_padrao_gdp}')
print(f'Coeficiente de Variação: {coeficiente_variacao_gdp}')

print('Quartis: ')
print(f'Primeiro Quartil: {primeiro_quartil_gdp}')
print(f'Segundo Quartil: {segundo_quartil_gdp}')
print(f'Terceiro Quartil: {terceiro_quartil_gdp}')

print()



