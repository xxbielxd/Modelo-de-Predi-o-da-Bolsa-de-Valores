import requests
from pandas import json_normalize
import pandas as pd

r = requests.get('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')
retorno_api = r.json()

arquivo = open('json.txt','w')
arquivo.write(str(retorno_api))


df = json_normalize(retorno_api) 

df['valor'] = pd.to_numeric(df['valor'])

print(df.query("data.str.contains('2022')")["valor"].sum())

#df.to_excel("output.xlsx")  

