# Predição na bolsa de valores 

A ideia inicial do projeto é tentar de alguma forma, usando variáveis externas, predizer se com a queda ou aumento dela,
irá influenciar, tanto positiva ou negativamente, a ação, tendo essa variável externa um alto índice de influência na ação.

No exemplo de predição, usamos a ação PETR4 (Petrobras). Pensando na ideia de que precisamos de variáveis que tenham um alto índice de influência 
na ação, utilizamos a taxa do SELIC e o preço do galão do petróleo. Além disso, utilizamos o valor da ação nos últimos 3 dias, para tentar encontrar 
algum padrão na ação que o algoritmo consigo predizer.

# Técnico

Usamos:
- deeplearnig(LSTM)
- API yahooquery, para retornar os dados da ação
- API do Banco Central, para retornar os dados da SELIC nos últimos anos (https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json)
- Pandas, para acessar os dados e manipular 
- matplotlib, para plotar os gráficos

Usamos várias outras ferramentas que o python dispõem, mas listamos os mais importantes.
