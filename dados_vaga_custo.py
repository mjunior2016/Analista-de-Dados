import pandas as pd
from sqlalchemy import create_engine

# Leitura dos dados
df = pd.read_csv('custos.csv',sep=';',encoding="ISO-8859-1")

#Criando colunas
colunas = list(df.columns)

#Adicionando Coluna Index
colunas.append('Index')

#Ordene os Id_cliente do maior para o menor
#Remova os valores NaN da coluna Custos
#Remova os valores inválidos da coluna Custos, mantendo somente os que podem ser convertidos em valores monetários
#Filtre os dados da coluna Data, removendo os registros dos anos de 2016 e 2022
query=''' 
    SELECT * FROM tablecusto
    WHERE Custos IS NOT NULL AND CAST(Custos AS INTEGER) IS Custos
    AND Data NOT LIKE '%2016' AND Data NOT LIKE '%2022'
    ORDER BY Id_cliente DESC 
'''

# Criação do banco de dados
engine = create_engine(r'sqlite:///bancovaga.db', echo=False)
df.to_sql('tablecusto', con=engine, if_exists='replace')
dados_db = engine.execute(query).fetchall()

#Criando Dataframe
df_sql = pd.DataFrame(dados_db, columns=[['Index','Id_cliente', 'Custos', 'Data']])

#Deletando Coluna 
df_sql.drop('Index', axis=1, inplace=True)

#Exportando dados custos para arquivo CSV
df_sql.to_csv('custostratado.csv',index=False)


