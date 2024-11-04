import pandas as pd

# Creacion de la variable que carga el archivo Excel y la hoja necesaria
# "C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/Redes_Sociales.xlsx" es la ruta en la que esta el EXCEL con los datos que se van a cargar 
datos = pd.read_excel('C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/Redes_Sociales.xlsx')
# Variable para el dataframe df_casos_bd
df_casos_bd = pd.read_excel('C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/df_casos_bd.xlsx')
# Variable para la hoja Meta
meta_df = pd.read_excel('C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/Redes_Sociales.xlsx', sheet_name='Meta')

# Se normalizan los valores en las columnas 'Red' y 'Tipo' para evitar problemas de coincidencia
meta_df['Red'] = meta_df['Red'].str.strip().str.lower()
meta_df['Tipo'] = meta_df['Tipo'].str.strip().str.lower()

# Unión de df_casos_bd con meta_df
df_casos_union = pd.merge(df_casos_bd, meta_df, on=['Red', 'Tipo'], how='left')
# Calcular el % de cumplimiento
df_casos_union['Cumplimiento'] = (df_casos_union['Cant_Casos'] / df_casos_union['Meta']) * 100
#Aproximar el % de cumplimiento al número entero más cercano
df_casos_union['Cumplimiento'] = df_casos_union['Cumplimiento'].round().astype(int)

# Exportación del dataframe df_casos_union a un archivo Excel
archivo = 'C:/Users/mateo/OneDrive/Desktop/PruebaTecnica/Prueba_tecnica_practicas/df_casos_union.xlsx'
df_casos_union.to_excel(archivo, index=False)