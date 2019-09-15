'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 04 : Herramientas Avanzadas de Visualización - Pie Charts
Fecha : 11/09/2019
Version : 1
Author : Jaime Gomez
Link : https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
'''
import matplotlib.pyplot as plt
import pandas as pd


print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.rename(columns={'Country': 'Pais'}, inplace=True)


# Pie chart
def basico_pie_charts():
    print("Cantidad de moviles vendidos-Agosto 2019")
    etiquetas = ['Samsung', 'Huawei', 'Apple',
                 'Xiaomi', 'HMD Global','Otros']
    valores = [18.3, 8.5, 6.4, 4.3, 1.2, 6.4]
    colores = [ 'green', 'red', 'blue',
                'purple','yellow', 'orange']
    plt.pie(valores, labels=etiquetas,
            colors=colores)
    plt.axis('equal') # ambos eje iguales
    #plt.savefig("C:\\Users\Alumno\PycharmProjects\sesion2_python\pie-01") # ubicación especifica
    plt.savefig("img/pie-02") # graba en la raiz
    plt.show()


def intermedio_pie_charts():
    'Cantidad de moviles vendidos hasta agosto del 2019'
    etiquetas = ['Samsung', 'Huawei', 'Apple',
                 'Xiaomi', 'HMD Global','Otros']
    valores = [18.3, 8.5, 6.4, 4.3, 1.2, 6.4]
    colores = [ 'green', 'red', 'blue', 'purple','yellow', 'orange']
    explode = [0, 0, 0.3, 0, 0.3, 0] # para resalta uno o mas valores del pie
    plt.title('Participación en las ventas del año 2019')
    plt.pie(valores, labels=etiquetas, colors=colores,
            explode=explode, startangle=-90) # startangle permite rotar la figura
                                             # explode permite separar uno o mas segmentos del pie
    plt.axis('equal')
    plt.savefig("img/pie-02_2")
    plt.show()

def avanzado_pie_charts():
    'Cantidad de moviles vendidos hasta agosto del 2019'
    font = {'family': 'serif',
            'color': 'green',
            'weight': 'normal',
            'size': 16,
            }
    etiquetas = ['Samsung', 'Huawei', 'Apple',
                 'Xiaomi', 'HMD Global','Otros']
    valores = [18.3, 8.5, 6.4, 4.3, 1.2, 6.4]
    colores = ['green', 'red', 'blue', 'purple','yellow', 'orange']
    explode = [0.1, 0, 0, 0, 0, 0]
    plt.title('Participación en ventas del año 2019',fontdict=font)
    plt.pie(valores, labels=etiquetas, colors=colores,
            explode=explode, shadow=True,autopct='%1.2f%%',
            startangle=90)
    #autopct = %1.2(cantidad digitos)f(tipo de datos )
    plt.axis('equal')
    plt.savefig("img/pie-03")
    plt.show()


def dataframe_basico_pie_plot():
    data = {'series1': [18.3, 8.5, 6.4, 4.3, 1.2, 6.4]}
    df = pd.DataFrame(data)
    df['series1'].plot(kind='pie')
    plt.axis('equal')
    plt.savefig("img/pie-04")
    plt.show()

def dataframe_intermedio_pie_charts():
    data = {'series1': [18.3, 8.5, 6.4, 4.3, 1.2, 6.4]}
    df = pd.DataFrame(data)
    colores = [ 'green', 'red', 'grey', 'purple','yellow', 'blue']
    df['series1'].plot(kind='pie',colors=colores)
    plt.savefig("img/pie-05")
    plt.show()


def dataframe_avanzado_pie_charts():
    font = {'family': 'serif',
            'color': 'red',
            'weight': 'normal',
            'size': 16,
            }
    colores = [ 'green', 'red', 'blue', 'purple','yellow', 'orange']
    explode = [0.1, 0, 0, 0, 0, 0]
    data = {'1': {"Samunsg":18.3, "Huawei":8.5, "Apple":6.4,
                        "Xiaomi":4.3, "HMD Global":1.2, "Otros":6.4}}
    df = pd.DataFrame(data)
    print(df)
    df['1'].plot(kind='pie',colors= colores, explode=explode,
                       shadow=True,autopct='%1.1f%%', startangle=90)
    plt.title('Participación en las ventas del año 2019',fontdict=font)
    plt.savefig("img/pie-06")
    plt.show()



#help(plt.title)
#help(plt.pie)

if __name__ == '__main__':

    #basico_pie_charts()
    #intermedio_pie_charts()
    #avanzado_pie_charts()
    #dataframe_basico_pie_plot()
    #dataframe_intermedio_pie_charts()
    dataframe_avanzado_pie_charts()