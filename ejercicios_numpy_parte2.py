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

def oper_matrices():

    # Arithmetic Operators
    #a_array = np.arange(4)
    a_array = np.ones((3,3))
    print(a_array)
    print(a_array + 4)
    print(a_array * 4)

def oper_matrices2():
    a_array = np.arange(4)
    b_array = np.arange(1,5)
    a_array = np.ones((3,3))*4
    b_array = np.ones((3,3))*8
    print("a:", a_array)
    print("b:", b_array)
    print("----Elemento por elemento----")
    print("Suma a+b: ", a_array + b_array)
    print("Resta a-b: ", a_array - b_array)
    print("Multiplicación a*b: ", a_array * b_array)

def oper_matrices3():
    a_matriz = np.arange(0, 16).reshape(4, 4)
    b_matriz = np.ones((4, 4))
    c_matriz = np.dot(a_matriz, b_matriz) #multiplicacion de matrices
    print("a_matriz : \n", a_matriz)
    print("b_matriz : \n", b_matriz)
    print("np.dot(a_matriz,b_matriz) : \n", c_matriz)


    a_matriz = np.arange(0, 16).reshape(4, 4)
    b_matriz = np.ones((4, 4))
    c_matriz = a_matriz.dot(b_matriz)
    print("a_matriz : \n",a_matriz)
    print("b_matriz : \n",b_matriz)
    print("a_matriz.dot(b_matriz) : \n", c_matriz)

def oper_matrices4():
    a_matriz = np.arange(0, 16).reshape(4, 4)
    print(a_matriz)
    #a_matriz =  a_matriz + 2
    a_matriz += 2
    print(a_matriz)

def oper_matrices5():

    a_matriz = np.arange(0,16).reshape(4,4) # no se afecta el origen a menos que se pida hacer eso con reemplazo.
    print(a_matriz)
    a_matriz_power = np.power(a_matriz, 2)
    print(a_matriz_power)
    print(a_matriz)
    print(a_matriz_power.sum())
    print(a_matriz_power.min())
    print(a_matriz_power.max())
    print(a_matriz_power.mean())

def ej_ope_matriz():
    a = np.ones((3,3))*4
    b = np.arange(0, 9).reshape(3, 3)
    print("a: ", a)
    print("b: ", b)
    c = a + b
    print("a+b: ", c)
    d = np.power(c,3)
    print("Matriz al cubo: \n", d)
    print("Elementos de matriz al cubo: ")
    print("1.Suma de Valores:" , d.sum())
    print("2.Menor elemento:" , d.min())
    print("3.Maximo elemento: ",d.max())
    print("4.Diferencia entre mayor y menor elemento es:" , d.max()-d.min())

def oper_matrices6():
    a_matriz = np.arange(0,16).reshape(4,4)
    r_cmatriz = np.apply_along_axis(np.mean,axis = 0 , arr=a_matriz) # axis --> indica 0 columnas / 1 filas
    r_fmatriz = np.apply_along_axis(np.mean, axis=1, arr=a_matriz)
    print(a_matriz)
    print(" ")
    print(r_cmatriz)
    print(r_fmatriz)
def inc(x):
    return  x+1

def oper_matrices7():
    a_matriz = np.arange(0,16).reshape(4,4)
    r_matriz = np.apply_along_axis(inc,axis = 1 , arr=a_matriz) # axis --> indica 0 columnas / 1 filas
    print(a_matriz)
    print(" ")
    print(r_matriz)

def impar(x):
    #p = 0
    if p % 2 != 0 :
        x[p] = -1
        p = p + 1
    p = p+1
    return  x



def oper_matrices8():
    a_matriz = np.arange(0,16).reshape(4,4)
    r_matriz = np.apply_along_axis(impar,axis = 1 , arr=a_matriz)
    print(a_matriz)
    print(" ")
    print(r_matriz)

def acceso_elementos():

    a_array = np.arange(0, 10)
    print("a_array        : ", a_array)
    print("a_array[0:5]   : ", a_array[0:5])
    print("a_array[0:5:2] : ", a_array[0:5:2])
    print("a_array[::2]   : ", a_array[::2])
    print("a_array[:5:2]  : ", a_array[:5:2])
    print("a_array[:5:]   : ", a_array[:5:])
    print("a_array[::3]   : ", a_array[::3])

def acceso_elementos2():

    a_matriz = np.arange(0,12).reshape(3,4)
    print("a_matriz : \n",a_matriz)
    print("a_matriz[:,0] : \n",a_matriz[:,0])
    print("a_matriz[0,:] : \n",a_matriz[0,:])
    print("a_matriz[0:2,0:2] : \n",
          a_matriz[0:2,0:2])
    print("a_matriz[[0,2],2:4] : \n",
          a_matriz[[0,2],2:4])
    print("a_matriz[1:3,2:4] : \n",
          a_matriz[1:3,2:4])
    print("a_matriz[[0,2,1],2:4] : \n",
      a_matriz[[0, 2,1], 2:4])


# Iterating an Array
def acceso_elementos3():
    a_array = np.arange(0,10)
    print("a_array :",a_array)
    for i in a_array:
        print(i)


def acceso_elementos4():
    a_matriz = np.arange(0,12).reshape(3,4)
    print("a_matriz : \n",a_matriz)

    for row in a_matriz:
        print("row --> ",row)

    for value in a_matriz.flat:
        print("value --> ",value)




#Funcion  principal
if __name__ == '__main__' :
    #oper_matrices()
    #oper_matrices2()
   # oper_matrices3()
    #oper_matrices4()
   # oper_matrices5()
    #ej_ope_matriz()
    #oper_matrices6()
    #oper_matrices7()
    #oper_matrices8() --> Falta

    #acceso_elementos2()
    acceso_elementos4()