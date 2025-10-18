import pandas as pd
import glob
import os

# Caminho onde estão os arquivos CSV
# Exemplo: "./dados/" (lembre de colocar a barra no final)
pasta = "C:\\Users\\William\\Desktop\\TCC M\\CSV"

# Padrão dos arquivos, ex: leptospirose_2014.csv, leptospirose_2014.csv, etc.
arquivos = glob.glob(os.path.join(pasta, "leptospirose_*.csv"))

# Lista pra armazenar todos os DataFrames
dfs = []

for arquivo in arquivos:
    # Extrai o ano do nome do arquivo (ex: leptospirose_2014.csv → 2014)
    ano = os.path.basename(arquivo).split("_")[-1].split(".")[0]

    # Lê o CSV (separador ; e com encoding comum em dados do SINAN)
    df = pd.read_csv(arquivo, sep=";", encoding="latin1")

    # Adiciona coluna do ano
    df["Ano"] = int(ano)

    # Adiciona à lista
    dfs.append(df)

# Junta tudo num só DataFrame
dados_completos = pd.concat(dfs, ignore_index=True)

# Corrige valores "-" para 0 e converte para números
dados_completos.replace("-", 0, inplace=True)
dados_completos.iloc[:, 1:-1] = dados_completos.iloc[:, 1:-1].apply(pd.to_numeric)

# Exibe as 10 primeiras linhas pra conferir
print(dados_completos.head(10))

# (Opcional) salva em um único CSV final
dados_completos.to_csv("leptospirose_2013_2023.csv", index=False, sep=";", encoding="utf-8-sig")
print("Arquivo final salvo como leptospirose_2013_2023.csv ✅")