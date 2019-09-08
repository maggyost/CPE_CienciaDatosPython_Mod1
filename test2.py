'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 03 : Herramientas Básicas de Visualización
Fecha : 08/09/2019
Version : 1
Author : Magaly Ostos R.
Tema   : Prueba_2

'''

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
America = ['Chile','Brazil','Argentina','Colombia','Peru','Bolivia','Ecuador','Paraguay','Uruguay','Mexico','Panama','Venezuela']
data = df.loc[America,'2018']
data = data.sort_values(ascending=True)
print(data)


def grafico_SurAmerica(): # Barras horizontales

    data.plot(kind='barh' , color='green')
    plt.title('Sur America')
    plt.xlabel('Billones de $')


    # annotate value labels to each country
    for index, value in enumerate(data):
        label = format(int(value), ',')  # format int with commas
        plt.annotate(label, xy=(value-5, index-0.1), color='black')

    plt.show()


if __name__ == '__main__':

    grafico_SurAmerica()