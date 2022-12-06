# Project Qualitron Revestimiento
# sql connection tools
# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import os

import pandas as pd
from dotenv import load_dotenv

from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import URL
from sqlalchemy.sql import text as sa_text

import sqlalchemy as db


# ----------------------------------------------------------------------------------------------------------------------
# SQL keys definition
# ----------------------------------------------------------------------------------------------------------------------
# Reading secrets
load_dotenv('../.env')

server = os.environ.get("SERVER")
database = os.environ.get("DATABASE")

table_calidad = os.environ.get("TABLE_CALIDAD")
table_defectos = os.environ.get("TABLE_DEFECTOS")

username = os.environ.get("USER_SQL")
password = os.environ.get("PASSWORD")

# ----------------------------------------------------------------------------------------------------------------------
# SQL connection definition
table = table_calidad
# ----------------------------------------------------------------------------------------------------------------------
# Connecting to the sql database
connection_str = "DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s" % (server, database, username, password)
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_str})

conn = create_engine(connection_url)

# ----------------------------------------------------------------------------------------------------------------------
# SQL execute
# ----------------------------------------------------------------------------------------------------------------------
# Read SQL
# pd_sql = pd.read_sql_query("SELECT * FROM " + database + ".dbo." + table + " WHERE fecha like '" + day + "'", conn)
pd_sql = pd.read_sql_query("SELECT * FROM " + database + ".dbo." + table, conn)

pd_sql.to_csv('test.csv', index=False)
# pd_sql.to_excel('BackUp_Agosto.xlsx', index=False)
# ----------------------------------------------------------------------------------------------------------------------
# Truncate table
# conn.execute(sa_text('''TRUNCATE TABLE %s''' % table).execution_options(autocommit=True))

# ----------------------------------------------------------------------------------------------------------------------
# Drop a column
# conn.execute(sa_text('''ALTER TABLE %s DROP COLUMN prueba_texto''' % table).execution_options(autocommit=True))

# ----------------------------------------------------------------------------------------------------------------------
# Modify a column
# conn.execute(sa_text('''ALTER TABLE %s ALTER COLUMN defecto VARCHAR(100)''' % table).execution_options(autocommit=True))

# ----------------------------------------------------------------------------------------------------------------------
# Adding a column
# conn.execute(sa_text('''ALTER TABLE %s ADD id_averia UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID()''' % table).execution_options(autocommit=True))
# conn.execute(sa_text('''ALTER TABLE %s ADD fecha_cierre DATE ''' % table).execution_options(autocommit=True))

# ----------------------------------------------------------------------------------------------------------------------
# Update a row
# conn.execute(sa_text('''UPDATE %s SET ciclo_cerrado = 1 WHERE id = '69794F53-0560-4BFD-92C6-C29E1374EDC7' ''' % table).execution_options(autocommit=True))

# ----------------------------------------------------------------------------------------------------------------------
# Drop a row
# conn.execute(sa_text('''DELETE FROM %s WHERE tecnico = 'Prueba' ''' % table).execution_options(autocommit=True))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Inspect table
inspector = inspect(conn)

for table_name in inspector.get_table_names():
    print(table_name)
    for column in inspector.get_columns(table_name):
        print(f"Column: {column['name']}, Type: {column['type']}")

# ----------------------------------------------------------------------------------------------------------------------
# Writing a row to SQL
# ----------------------------------------------------------------------------------------------------------------------
fecha = '2022-11-17 00:43:35'
planta = 'Madrid'
qualitron = 'MD_9'
producto = 'Prueba'
calidad = 'Primera'

# ----------------------------------------------------------------------------------------------------------------------
# To table calidadGeneral
tono = 'FT'
valor_unidad = 25

columns_name = ['fecha', 'planta', 'qualitron', 'producto', 'tono', 'calidad', 'valor_unidad']

# Datos a enviar
data = [fecha, planta, qualitron, producto, tono, calidad, valor_unidad]

# ----------------------------------------------------------------------------------------------------------------------
# To table defectosGeneral
# defecto = 'Defecto'
# valor_unidad = 30

# columns_name = ['fecha', 'planta', 'qualitron', 'producto', 'calidad', 'defectos', 'valor_unidad']

# Datos a enviar
# data = [fecha, planta, qualitron, producto, calidad, defecto, valor_unidad]

# ----------------------------------------------------------------------------------------------------------------------
# Pandas Creation
df = pd.DataFrame(data=data).T
df.columns = columns_name

# To SQL
#df.to_sql(table, conn, if_exists='append', index=False)


