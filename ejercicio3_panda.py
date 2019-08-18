'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 04 : Pandas: Manipulacion de datos - Leer archivos
Fecha : 10/08/2019
Version : 1
Author :
'''

#
#import abc as nueva libreria

#import abriloge_python as abrilcolage

# facilita la lectura


import pandas as pd

# Leer archivo csv
print("---------------------------------")
archivo_csv = "medallero_Panamericanos_Lima2019.csv"
df = pd.read_csv(archivo_csv)
print("==============head:valores de 05 filas==========")
print(df.head())
print("==============keys: cabeceras en lista==========")
print(df.keys())

# Leer un campo del archivo csv : Series
print("---------------------------------")
col_pais = df['Pais']
print(type(col_pais))
print(col_pais)

# Leer un campo del archivo csv : DataFrame
print("=======================================")
medallas = df[['Pais','Oro','Plata','Bronce','Total']]
print(type(medallas))
print(medallas)

print("============iloc===========================")
#Primera columna
X= 0
dato = df.iloc[:,X]
print(dato)

X= 1
dato = df.iloc[:,0:3]
print(dato)

# mostrar el segmento de los data frame
dato = df.iloc[0:2,0:3]
print(dato)

#
print("---------------loc------------------")

print(df.head())

df.set_index("Pais", inplace=True)
print(df.head())

dato = df.loc["Brasil"]
print(type(dato))
print(dato)



