import pandas as pd

# Creacion de la variable que carga el archivo Excel y la hoja necesaria
# "C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/Redes_Sociales.xlsx" es la ruta en la que esta el EXCEL con los datos que se van a cargar 
datos = pd.read_excel('C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/Redes_Sociales.xlsx') 
# Variable para la hoja Casos
casos_df = pd.read_excel('C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/Redes_Sociales.xlsx', sheet_name='Casos')

# Se normalizan los valores en las columnas 'Red' y 'Tipo' para evitar problemas de coincidencia
casos_df['Red'] = casos_df['Red'].str.strip().str.lower()
casos_df['Tipo'] = casos_df['Tipo'].str.strip().str.lower()

# Hace la transformación del DataFrame de "casos_df" al formato df_casos_bd
df_casos_bd = casos_df.melt(id_vars=["Red", "Tipo"], var_name="Fecha", value_name="Cant_Casos")
# Se ajusta el formato de la columna "Fecha" para mostrarlo como DD/MM/YY
df_casos_bd['Fecha'] = pd.to_datetime(df_casos_bd['Fecha']).dt.strftime('%d/%m/%Y')
# Rellenar las celdas de la columna 'Red' que estén en blanco
df_casos_bd['Red'] = df_casos_bd['Red'].ffill()

# Exportación del DataFrame a un archivo Excel
archivo = 'C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/df_casos_bd.xlsx'
df_casos_bd.to_excel(archivo, index=False)