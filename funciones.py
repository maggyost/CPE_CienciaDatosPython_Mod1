'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 03 : Fundamentos de programación - Function
Fecha : 21/07/2019
Version : 1
Author :
'''

def inc(a):
    b= a +1
    return(b)

valor = inc(2)
print(valor)



def suma(dato1,dato2):
    s = dato1 + dato2
    return s

resultado = suma(3,7)
print(resultado)

print("======Funcion de Suma de N====Formula===== ")

def suma_n(n):
    resultado = n*(n+1)/2
    return resultado

n = int(input("Ingrese n, numero entero: "))
valor = suma_n(n)
print(valor)



print("======Funcion de Suma de N=====For==== ")

def sum_for(n):
    i = 1
    suma = 0
    LIMITE = n
    for i < LIMITE :
        suma = suma + i
        i = i + 1
    return suma


resultado1 = sum_for(3)

print ( resultado1)