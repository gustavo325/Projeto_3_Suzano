import requests
import pandas as pd 

#Consumo da API (importação dos dados) 
exemple = requests.get("http://localhost:3000/api/ep1")

dados = exemple.json()

df = pd.DataFrame(dados) 
print(df["date"]) 