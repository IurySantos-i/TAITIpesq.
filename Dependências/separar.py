


# Importar o módulo pandas
import pandas as pd

# Ler o arquivo csv original como um dataframe
df = pd.read_csv("tasks_data_990(1).csv", error_bad_lines=False)

# Obter os valores únicos da primeira coluna
categories = df.iloc[:, 0].unique()

# Iterar sobre as categorias
for category in categories:
    # Filtrar o dataframe pela categoria
    df_category = df[df.iloc[:, 0] == category]
    # Criar um nome de arquivo baseado na categoria
    filename = f"{category}.csv"[19:]
    # Salvar o dataframe filtrado como um arquivo csv
    df_category.to_csv(r"F:\Pesquisa TAITI\Dependências\{filename}.csv", index=False)
