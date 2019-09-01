'''

'''

import pandas as pd
import numpy as np

df = pd.read_csv("medallero_Panamericanos_Lima2019.csv")

def calc_suma():

#print(df.head())
    print(df['Oro'].sum())
    print(df.Oro.sum())

    print(np.sum(df['Oro']))  # con numpy
    print(np.sum(df.Oro))


def calc_nro_elementos():
    print(len(df['Oro']))
    print(len(df.Oro))
    print(df['Oro'].count())
    print(df.Oro.count())
    print(np.size(df.Oro))
    print(np.size(df['Oro']))

def calc_media():
    print(np.mean(df.Oro))  # numpy
    print(df.Oro.sum()/df.Oro.count()) # usando pandas
    print(df.Oro.mean()) # pandas


def obtener_media(redondeo=2):
    media = df.Oro.mean()
    media = round(media,redondeo)
    return media


def cal_mediana():
    print("---------------------------------")
    mediana = df['Oro'].median()
    nro_item = np.size(df['Oro'])
    pos_mediana = round(nro_item/2)
    print("pos_mediana = ", pos_mediana)
    print("mediana manual = ",
          df['Oro'][pos_mediana-1])
    print("mediana = ", mediana)

def cal_mediana_plata():
    print("---------------------------------")
    plata_sort = np.sort(df.Plata)
    print(plata_sort)
    print(type(plata_sort))
    nro_item = np.size(plata_sort)
    pos_mediana = round(nro_item/2)
    print("pos_mediana = ", pos_mediana)
    print("mediana manual = ",
          plata_sort[pos_mediana-1])
    mediana = np.median(plata_sort)
    print("Mediana PLata= ", mediana)

def cal_mediana_Bronce():
    print("---------------------------------")
    bronce_sort = np.sort(df.Bronce)
    print(bronce_sort)
    print(type(bronce_sort))
    nro_item = np.size(bronce_sort)
    pos_mediana = round(nro_item/2)
    print("pos_mediana = ", pos_mediana)
    print("mediana manual = ",
          bronce_sort[pos_mediana-1])
    mediana = np.median(bronce_sort)
    print("Mediana Bronce= ", mediana)

def obtener_mediana():
    nro_item = np.size(df.Oro)
    pos_mediana = round(nro_item/2)
    mediana = df.Oro[pos_mediana-1]

#   mediana = np.median(df.Oro)

#   median = np.Oro.median()

    return mediana

def obtener_moda():

    moda = df.Oro.mode()

    return moda

def cal_percentiles():
    print("---------------------------------")
    tramos = [25,50,75]
    percentiles = np.percentile(df['Oro'],tramos)
    print("percentiles = ", percentiles )

# Grafico Percentiles
def graph_percentiles():
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.boxplot(y="Oro", data= df)
    plt.show()

#Varianza
def cal_varianza():
    diff = df[['Oro']] - df['Oro'].mean()
    print(type(diff))
    diff2 = np.power(diff,2)
    print(type(diff2))
    nro_item = np.size(df['Oro'])
    var_manual = (diff2.sum()/nro_item)['Oro']
    #print(type(var_manual))
    print("varianza manual = ", var_manual)

    var = df['Oro'].var(ddof=0)  # corrección de Bessel 1/n-1
    print("varianza = ", var)
    print("varianza = ", np.var(df['Oro']))

def cal_varianza_plata():

    diff = df['Plata'] - df['Plata'].mean()
    diff2 = np.power(diff,2)
    nro_item = np.size(df['Plata'])
    var_manual = (diff2.sum() / nro_item)
    print("varianza manual Plata = ", var_manual)

def cal_desviacion_estandar():

    std_manual = np.sqrt(df.Oro.var(ddof=0))
    print("Desviacion_Estandar = ", std_manual)

#Funcion  principal
if __name__ == '__main__' :
    #calc_suma()
    #calc_nro_elementos()
    #calc_media()
    #print(obtener_media())
    #print(obtener_media(4)) # imprimo toda la función por tratarse de un return
    #print(df.mean()) # solo aplica a los valores
    #print(round(df.mean(),2)) # aplica a todos los valores
    #cal_mediana()
    #print(obtener_mediana())
    #cal_mediana_plata()
    #cal_mediana_Bronce()
    #print(obtener_moda())
    #print(df.Oro.value_counts()) # indica 1 medalla obtiene 8 personas
    #cal_percentiles()
    #graph_percentiles()
    #cal_varianza()
    cal_varianza_plata()
    cal_desviacion_estandar()
    print(df.describe())



