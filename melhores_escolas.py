#importando o pandas
import pandas as pd

#colocando os dados em um variavel 
schools = pd.read_csv("schools.csv")

#vendo os dados
schools.head()

#Ponto 01
#Criando o dataframe best_math_schools baseado no df schools e filtrando os valores
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)

#Ponto 02
#Criando a coluna total_SAT
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
#Criando o df top_10_schools
top_10_schools = schools.sort_values("total_SAT", ascending=False)[["school_name", "total_SAT"]].head(10)

#Ponto 03
# Adicionando a coluna total_SAT ao dataframe schools
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]

# Qual bairro teve maior desvio padrão
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

#Filtrar por desvio padrão max e criar a coluna bairros
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Renomear as colunas
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})