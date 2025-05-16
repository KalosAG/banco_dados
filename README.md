# banco_dados
Implementação do banco de dados[Interfaces de programação - 2025.1]

Construção do banco de dados utilizando a biblioteca sqlalchemy coletando os dados públicos da saúde

OBJ: Coletar dados, tratar, correlacionar com o banco

---

1. Instalar bibliotecas 

````
pip install folium
pip install sqlalchemy
````

2. Criar ambiente postgresql por meio do sqlalchemy

```
from sqlalchemy import create_engine
engine = create_engine('postgresql://username:password@localhost:5432/dbname')
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM your_table")
    for row in result:
        print(row)
```

## Folium
### Vai ser usado por conta de sua criação de templates que já podem ser integrados com o sistema do flask

## Sqlalchemy
### Utilizado para criar uma engine postgresql, escolhido pela fácil administração do dataset

---

# Objetivos indicados pelo professor(2º mês)
# R2 Apresentação - Projeto 3.2 SESA


Simular os seguintes dados para o BI:

- **12 tipos de enfermidade**
- **20 a 25 em cada enfermidade**
- **Custo de tratamento de cada pessoa por enfermidade**
- **Tempo de tratamento de cada pessoa na enfermidade**
- **3 tipos de faixa etária das pessoas cadastradas:**
  - Idoso (≥60 anos)
  - Crianças (≤10 anos)
  - Outros (entre 11 e 59 anos)
- **Usar 10 cidades distintas**

Os dados devem ser simulados para o interstício de 2 anos em cada cidade.
