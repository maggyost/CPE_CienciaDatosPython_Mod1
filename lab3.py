'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 03 : Fundamentos de programación - Lab03
Fecha : 21/07/2019
Version : 1
Author : Magaly Ostos
'''

with open("operaciones.txt","r") as archivo:
    suma = 0
    for i in range(3) :
        contenido = archivo.readline()
        valor = int(contenido[4:8])
        suma = suma + valor
    print(suma)

