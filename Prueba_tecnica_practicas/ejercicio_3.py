import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos MySQL
conexion = create_engine('mysql+mysqlconnector://root:@localhost/bd_prueba_tec')
# Cargar el DataFrame df_casos_union
df_casos_union = pd.read_excel('C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/df_casos_union.xlsx')
# Insertar datos en la tabla
df_casos_union.to_sql(name='df_casos_union', con=conexion, if_exists='replace', index=False)
# Consulta SQL
query = """
SELECT Red, Tipo, 
       YEAR(STR_TO_DATE(Fecha, '%d/%m/%Y')) AS Año, 
       MONTH(STR_TO_DATE(Fecha, '%d/%m/%Y')) AS Mes, 
       SUM(Cant_Casos) AS Cant_Casos
FROM df_casos_union
GROUP BY Red, Tipo, Año, Mes;
"""
# Ejecutar la consulta y cargar el resultado en un DataFrame
df_resultado = pd.read_sql_query(query, con=conexion)

# Guardar el DataFrame en un archivo Excel
consulta = 'C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/resultado_consulta.xlsx'
df_resultado.to_excel(consulta, index=False)