'''
Programa: Ciencia de Datos con Python
Modulo: Fundamentos Python
Sesion 02: Introducción - String
Fecha: 04/08/2019
Version: 1
Autor : Magaly Ostos
'''

msg = "Panam"
msg = msg + " Sports "
year = 2019
year = str(2019)
msg = msg + year # Se suman mismos tipos de datos

print(msg)
print("--->",msg,": ",year)

print("====================")
msg ="a123456789"
print(msg)
print(len(msg))
print(msg[0])
print(msg[5])
print(msg[-1])
print(msg.upper())
msg_1 = str.upper(msg)
print(msg_1)

print("=========Ingreso de Datos===========")
'''
s = input("Ingrese Datos : ")
print("Mostrar Datos: ",s)
'''
num1 = input("Ingrese Número 1: ")
num2 = input("Ingrese Número 2: ")
suma= int(num1)+int(num2)
print ( "La Suma de los números es: ", suma)


a = float(input("Ingrese Número 1: "))
b = float(input("Ingrese Número 2: "))
suma1= a +b

print("La suma es: ", suma1)