'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 03 : Lab02
Fecha : 21/07/2019
Version : 1
Author :Magaly Ostos
'''


print("======Funcion de Suma de N====Formula===== ")

def suma_n(n):
    resultado = n*(n+1)/2
    return resultado

n = int(input("Ingrese n, numero entero: "))
valor = suma_n(n)
print(valor)

