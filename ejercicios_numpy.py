'''
Programa : Ciencia de Datos con Pthon
Modulo 02 : Estadística y Visualización de Datos con Python
Sesion 01 : Examples con numpy
Fecha : 25/08/2019
Version : 1
Author : Magaly Ostos
Tema: numpy ( numerico python )
'''

import numpy as np  # Alias

def ej_numpy() :

    mi_lista = [1,2,3]   # lista
    a = np.array(mi_lista) # usa np.array para transformat es array = matriz
    print(type(mi_lista))
    print(mi_lista)
    print(type(a))
    print(a) # el np lo transforma en matriz
    # El objeto mas usado es ndarray

    print(type(a))
    print("nro_array --> ",a)
    print("dtype --> ",a.dtype)
    print("ndim --> ",a.ndim)
    print("size --> ",a.size)
    print("shape --> ",a.shape)

    print("itemsize --> ",a.itemsize)
    print("data --> ",a.data)

    print("------lista2-------")
    mi_lista = [[1,2,3],[4,5,6]]
    a = np.array(mi_lista)
    print(type(a))
    print("nro_array --> ",a)
    print("dtype --> ",a.dtype)
    print("ndim --> ",a.ndim)  # dimensiones de matriz
    print("size --> ",a.size) # valores totales
    print("shape --> ",a.shape) #
    print("itemsize --> ",a.itemsize)
    print("data --> ",a.data)

#help(np.dtype)

def ej2_numpy():
    nro_array = np.array([[1,2,3],[4,5,6]])
    print(nro_array)

def ej3_numpy():
    ceros_array = np.zeros((3, 3))
    print("np.zeros((3,3)) --> ", ceros_array)

    unos_array = np.ones((3, 3))
    print("np.ones((3,3)) --> ", unos_array)

    nros_array = np.arange(8)
    print("np.arange(8) --> ", nros_array)

    nros_array = np.arange(3, 8)
    print("np.arange(3,8) --> ", nros_array)

    nros_array = np.arange(1, 16, 3)
    print("np.arange(1,16,3) --> ", nros_array)

    nros_array = np.arange(0, 15).reshape(5, 3)
    print("np.arange(0,15).reshape(5,3) --> ", nros_array)

    nros_array = np.linspace(0, 15, 7)
    print("np.linspace(0,15,7) --> ", nros_array)

    nros_array = np.random.random(4)
    print("np.random.random(4) --> ", nros_array)

    nros_array = np.random.random((2, 3))
    print("np.random.random((2,3)) --> ", nros_array)

def generar_matriz() :
    fin = 21 + (4*4-1)*2 + 1  # para no pensar en el fin del arange
    matriz = np.arange(21, fin,2).reshape(4,4 ) #indica 16 elementos
    print(matriz)

if __name__ == '__main__' :
    #print('---ejemplo1---')
    #ej_numpy()
    #print('----ejemplo2---')
    #ej2_numpy()
    #print('----ejemplo3---')
    #ej3_numpy()
    generar_matriz()