import pandas as pd 

df = pd.read_csv("dataset_evasao_escolar_500_registros_com_valores_faltantes.csv")

# 1.
# a)

# 500 registros, 17 atributos
# print(f"{df.shape}\n")

# Nome dos atributos
# print(f"{df.columns}\n")

# Todos os dados são do tipo object, 
# provavelmente porque mesmo as colunas numéricas tem strings e valores em branco...
# print(f"{df.dtypes}\n")

# print(f"{df.head()}\n")

# print(f"{df.info()}\n")

# print(f"{df.describe()}\n")

# b)
# idade -> dado quantitativo discreto, espera um número inteiro maior ou igual a 0
# escola_origem -> dado qualitativo nominal, classificação entre "Pública" e "Privado"
# municipio_residencia -> dado qualitativo nominal, espera o nome da cidade no formato "Marechal Deodoro"
# estado_residencia -> dado qualitativo nominal, espera a abreviação do estado no formato AL, PE etc
# renda_familiar_mensal -> dado quantitativo contínuo, espera um valor numérico com até duas casas decimais

# 2. 
# a)

# Percentual dos valores ausentes em cada atributo
# for row in df:
    # print(row)
    # print(f"Quantity: {df[row].isnull().sum()}")
    # print(f"Percentage: {df[row].isnull().mean() * 100}%")
    # print()

# b)
# Valores Nulos
stats = df.describe()

# ['A0326', 'A0311', 'A0120', 'A0093', 'A0127', 'A0441', 'A0087', 'A0256', 'A0013', 'A0100', 'A0429', 'A0151', 
# 'A0353', 'A0126', 'A0021', 'A0230', 'A0440', 'A0272', 'A0342', 'A0397', 'A0169', 'A0052', 'A0436', 'A0136', 
# 'A0199', 'A0322', 'A0233', 'A0467', 'A0082', 'A0376']
ids_repetidos = df.loc[df["id_aluno"].duplicated(), 'id_aluno'].unique().tolist()

print(len(ids_repetidos))