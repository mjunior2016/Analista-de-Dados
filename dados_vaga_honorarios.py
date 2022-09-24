import pandas as pd

# Leitura de dados
df_grupos = pd.read_excel('dados.xlsx','grupos')

# Excluindo coluna Indice
df_grupos.drop(columns=['Índice'],inplace=True)

#Renomeando Coluna
df_grupos.rename(columns={'Tipo_cliente':'Id_tipo_cliente'},inplace=True)

# Leitura de dados
df_tipocliente = pd.read_excel('dados.xlsx','tipo_cliente')

# Leitura de dados
df_hono = pd.read_csv('honorarios.csv',sep=';',encoding="ISO-8859-1")

# Retirar indice
df_hono.reset_index(drop=True)

# Remover agente 8000
df_hono = df_hono.drop(index=df_hono[df_hono['Agente']==8000].index)

# Remover valores nulo
df_hono = df_hono.dropna(how='all')

#Concatenando dados honorarios com dados de grupos
mergedf = df_hono.merge(df_grupos,how='left',on='Id_cliente')

#Concatenando resultado de honorarios + grupos com tipo cliente
mergedf2 = pd.merge(mergedf,df_tipocliente[['Id_tipo_cliente','Tipo_cliente']],on=['Id_tipo_cliente'],how='left')

#Excluindo Tipo cliente igual a terceirado
honorarios  = mergedf2.drop(index=mergedf2[mergedf2['Tipo_cliente']=='Terceirizado'].index)

#Exportando para o Arquivo CSV
honorarios.to_csv('honorariostratado.csv',index=False)
