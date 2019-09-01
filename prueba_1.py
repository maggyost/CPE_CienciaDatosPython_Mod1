'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 02 : Prueba_1
Fecha : 1/09/2019
Version : 1
Author : Magaly Ostos
Tema: Prueba_1 :
crear funcioan estadisticos donde los valores son:
list_1 = obtener_estadisticos("Oro")
count
mean
media
var
std
min
max
usar tupla o lista

'''

import pandas as pd
import numpy as np

df = pd.read_csv("medallero_Panamericanos_Lima2019.csv")

def obtener_estadisticos( columna, redondeo=4 ):

    cuenta = df[columna].count()
    media = round(df[columna].median(), redondeo)
    mediana = round(df[columna].mean(),redondeo)
    var = round(df[columna].var(ddof = 0 ),redondeo)
    std = round(np.sqrt(var),redondeo)
    min = df[columna].min()
    max = df[columna].max()

    list_1 = [cuenta,media,mediana,var,std,min,max]


    return list_1



if __name__ == '__main__' :

    print (obtener_estadisticos("Oro"))
    print(type(obtener_estadisticos("Oro")))
    print("Valores estadistico: ", )
    print("Cuenta = ",obtener_estadisticos("Oro")[0])
    print("Media = ", obtener_estadisticos("Oro")[1])
    print("Mediana = ", obtener_estadisticos("Oro")[2])
    print("Varianza = ", obtener_estadisticos("Oro")[3])
    print("Desviación_Estandar = ", obtener_estadisticos("Oro")[4])
    print("Valor_Min = ", obtener_estadisticos("Oro")[5])
    print("Valor_Max = ", obtener_estadisticos("Oro")[6])

