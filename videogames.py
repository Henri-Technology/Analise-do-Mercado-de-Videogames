import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Define para mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Load the dataset
df_videogames = pd.read_csv("./code/videogames-limpo.csv")

# Verificar os tipos de dados



# Transfor dados
df_videogames = df_videogames.rename(columns={
    'total_sales': 'Total Vendas (MI)',
    'critic_score': 'Pontuacao Critica',
    'release_year': 'Ano de Lancamento',
    'genre': 'Genero',
    'console': 'Console',
    'publisher': 'Empresa Publicadora',
    'developer': 'Desenvolvedora',
    'title': 'Titulo do Jogo'
    })



# Definimos os limites: 0-40 (Ruim), 40-70 (Regular), 70-100 (Bom)
bins = [0, 4.0, 7.0, 10.0]
labels = ['Ruim', 'Regular', 'Bom']

df_videogames['Classificacao'] = pd.cut(df_videogames['Pontuacao Critica'], bins=bins, labels=labels)



#Total vendas por empresa Publicadora
vendas_por_empresa = df_videogames.groupby('Empresa Publicadora')['Total Vendas (MI)'].sum().sort_values(ascending=False).head(10)
print("\nTotal vendas por empresa Publicadora:")
print(vendas_por_empresa)

#total vendas por console
vendas_por_console = df_videogames.groupby('Console')['Total Vendas (MI)'].sum().sort_values(ascending=False).head(10)
print("\nTotal vendas por console:")
print(vendas_por_console)

# total vendas por genero
vendas_por_genero = df_videogames.groupby('Genero')['Total Vendas (MI)'].sum().sort_values(ascending=False).head(10)
print("\nTotal vendas por genero:")
print(vendas_por_genero)

#total vendas por ano de lancamento
vendas_por_ano = df_videogames.groupby('Ano de Lancamento')['Total Vendas (MI)'].sum().sort_values(ascending=False)
print("\nTotal vendas por ano de lancamento:")
print(vendas_por_ano)

#total vendas por titulo
vendas_por_titulo = df_videogames.groupby('Titulo do Jogo')['Total Vendas (MI)'].sum().sort_values(ascending=False).head(10)
print("\nTotal vendas por titulo:")
print(vendas_por_titulo)

#Media
#media de vendas por empresa publicadora
media_vendas_por_empresa = df_videogames.groupby('Empresa Publicadora')['Total Vendas (MI)'].mean().sort_values(ascending=False).head(10)
print("\nMédia de vendas por empresa publicadora:")
print(media_vendas_por_empresa)

#media de vendas por console
media_vendas_por_console = df_videogames.groupby('Console')['Total Vendas (MI)'].mean().sort_values(ascending=False).head(10)
print("\nMédia de vendas por console:")
print(media_vendas_por_console)

#media de vendas por genero
media_vendas_por_genero = df_videogames.groupby('Genero')['Total Vendas (MI)'].mean().sort_values(ascending=False).head(10)
print("\nMédia de vendas por genero:")
print(media_vendas_por_genero)

#media de vendas por ano de lancamento
media_vendas_por_ano = df_videogames.groupby('Ano de Lancamento')['Total Vendas (MI)'].mean().sort_values(ascending=False)
print("\nMédia de vendas por ano de lancamento:")
print(media_vendas_por_ano)

#media de vendas por titulo
media_vendas_por_titulo = df_videogames.groupby('Titulo do Jogo')['Total Vendas (MI)'].mean().sort_values(ascending=False).head(10)
print("\nMédia de vendas por titulo:")
print(media_vendas_por_titulo)



#quantos titulos diferntes exitem para cada empresa publicadora tem
titulos_por_empresa = df_videogames.groupby('Empresa Publicadora')['Titulo do Jogo'].nunique().sort_values(ascending=False).head(10)
print("\nNúmero de títulos por empresa publicadora:")
print(titulos_por_empresa)

#quantos jogos foram lançados desde 1980 até 2020
jogos_por_ano = df_videogames['Titulo do Jogo'].nunique()
print("\nNúmero de jogos lançados por ano:")
print(jogos_por_ano)

#Grafico de vendas por empresa publicadora
plt.figure(figsize=(12, 6))
sns.barplot(x=vendas_por_empresa.index, y=vendas_por_empresa.values)
sns.color_palette("Paired")
plt.title('Total de Vendas por Empresa Publicadora')
plt.xlabel('Empresa Publicadora')
plt.ylabel('Total de Vendas (MI)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafico de vendas por console
plt.figure(figsize=(12, 6))
sns.barplot(x=vendas_por_console.index, y=vendas_por_console.values)
sns.color_palette("Paired")
plt.title('Total de Vendas por Console')
plt.xlabel('Console')
plt.ylabel('Total de Vendas (MI)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafico de vendas por genero
plt.figure(figsize=(12, 6))
sns.barplot(x=vendas_por_genero.index, y=vendas_por_genero.values)
sns.color_palette("Paired")
plt.title('Total de Vendas por Genero')
plt.xlabel('Genero')
plt.ylabel('Total de Vendas (MI)')
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()

#Grafico de vendas por ano de lancamento
plt.figure(figsize=(12, 6))
sns.barplot(x=vendas_por_ano.index, y=vendas_por_ano.values)
sns.color_palette("Paired")
plt.title('Total de Vendas por Ano de Lancamento')
plt.xlabel('Ano de Lancamento')
plt.ylabel('Total de Vendas (MI)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafico de previsão de vendas por ano de lancamento
plt.figure(figsize=(12, 6))
sns.lineplot(x=vendas_por_ano.index, y=vendas_por_ano.values)
sns.color_palette("Paired")
plt.title('Tendência Histórica de Vendas por Ano de Lancamento')
plt.xlabel('Ano de Lancamento')
plt.ylabel('Total de Vendas (MI)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafico de vendas médias por classificação e gênero
top_generos = df_videogames.groupby('Genero')['Total Vendas (MI)'].sum().nlargest(10).index
df_grafico6 = df_videogames[df_videogames['Genero'].isin(top_generos)]

plt.figure(figsize=(12, 6))

# O segredo: 'estimator=sum' faz as barras aparecerem acumuladas
# 'ci=None' remove aquelas linhazinhas de erro pretas que sujam o gráfico
sns.barplot(
    data=df_grafico6, 
    x='Genero', 
    y='Total Vendas (MI)', 
    hue='Classificacao', 
    hue_order=['Ruim', 'Regular', 'Bom'],
    estimator=sum,
    errorbar=None
)

plt.title('Total de Vendas por Gênero e Classificação (Top 10 Gêneros)')
plt.xlabel('Gênero')
plt.ylabel('Vendas Acumuladas (Milhões)')
plt.xticks(rotation=45)

# Ajusta a legenda para fora do gráfico para não tampar as barras
plt.legend(title='Avaliação', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()


#Quantidade de jogos por Classificação ao longo do tempo
# 1. Garante que o ano é inteiro para tirar o ".0"
df_videogames['Ano de Lancamento'] = df_videogames['Ano de Lancamento'].fillna(0).astype(int)

# 2. Cria a década e filtra anos irrelevantes (como o 0)
df_videogames['Decada'] = (df_videogames['Ano de Lancamento'] // 10 * 10).astype(str) + "s"
df_decadas = df_videogames[df_videogames['Ano de Lancamento'] > 1970].sort_values('Ano de Lancamento')

plt.figure(figsize=(12, 6))

# Countplot para contar a quantidade de jogos
sns.countplot(
    data=df_decadas, 
    x='Decada', 
    hue='Classificacao', 
    hue_order=['Ruim', 'Regular', 'Bom']
)

plt.title('Quantidade de jogos por Classificação ao Longo do Tempo')
plt.ylabel('Quantidade de Jogos')
plt.legend(title='Classificação')
plt.tight_layout()
plt.show()