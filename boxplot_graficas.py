'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 04 : Herramientas Avanzadas de Visualización - Box Plot
Fecha : 11/09/2019
Version : 1
Author : Jaime Gomez
Link : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html
       https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.rename(columns={'Country': 'Pais'}, inplace=True)
'''
#
def basico_box_plot():
    'Diagrama de caja'
    nota_matematica = [18,15,20,15,14,11,16,
                       1,20,19,19]
    print(nota_matematica)
    plt.boxplot(nota_matematica,
                labels=["Matemáticas"])
    plt.title("Diagrama de Cajas")
    plt.ylabel("Notas")
    plt.savefig("img/boxplot-01")
    plt.show()

def basico_box_plot_2():
    'Diagrama de caja'
    nota_matematica = [10,15,20,15,5,5,5,10,19,19,19]
    print(nota_matematica)
    plt.boxplot(nota_matematica, labels=["Matemáticas"], vert=False)
    plt.title("Diagrama de Cajas")
    plt.xlabel("Notas")
    plt.savefig("img/boxplot-02")
    plt.show()


def intermedio_box_plot():
    'Diagrama de caja'
    nota_matematica = [10,15,20,15,5,5,5,10,19,19,19]
    nota_lenguaje = [3,5,7,6,7,8,5,7,10,8,19]
    nota_historia = [19,18,17,12,17,18,15,3,10,18,19]
    etiqueta = ["Matematica","Lenguaje","Historia"]
    data = [nota_matematica,nota_lenguaje, nota_historia]
    print(type(data))
    print(nota_matematica)
    plt.boxplot(data, labels=etiqueta)
    plt.title("Diagrama de Cajas")
    plt.ylabel("Notas")
    plt.savefig("img/boxplot-03")
    plt.show()


def dataframe_basico_box_plot():
    data = {'Matematica': [10,15,20,15,5,5,5,10,19,19,19]}
    df = pd.DataFrame(data)
    df['Matematica'].plot(kind='box')
    plt.title("Diagrama de Cajas")
    plt.ylabel("Notas")
    plt.savefig("img/boxplot-05")
    plt.show()


def dataframe_intermedio_box_plot():
    data = {'Matematica': [10,15,20,15,5,5,5,10,19,19,19],
            'Lenguaje': [3,5,7,6,7,8,5,7,10,8,19],
            'Historia': [19,18,17,12,17,18,15,3,10,18,19]}
    df = pd.DataFrame(data)
    df.plot(kind='box')
    plt.title("Diagrama de Cajas")
    plt.ylabel("Notas")
    plt.savefig("img/boxplot-06")
    plt.show()




if __name__ == '__main__':
    #basico_box_plot()
    #basico_box_plot_2()
    intermedio_box_plot()