# banco_dados
Implementação do banco de dados[Interfaces de programação - 2025.1]

Construção do banco de dados utilizando a biblioteca sqlalchemy coletando os dados públicos da saúde

OBJ: Coletar dados, tratar, correlacionar com o banco

----------------------------------------------------------------------------------------------------------------------------------------------

# Instlar bibliotecas 

`pip install folium`

`pip install sqlalchemy`



`from sqlalchemy import create_engine`

`engine = create_engine('postgresql://username:password@localhost:5432/dbname')`

`with engine.connect() as connection:`

    `result = connection.execute("SELECT * FROM your_table")`
    
    `for row in result:`
    
        `print(row)`

## Folium
### Vai ser usado por conta de sua criação de templates que já podem ser integrados com o sistema do flask

## Sqlalchemy
### Utilizado para criar uma engine postgresql, escolhido pela fácil administração do dataset
