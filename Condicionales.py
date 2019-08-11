'''
valor = input("Ingresar un número entero: ")
num = int(valor)
if num%2 == 0 :
    print("El número es par")

else:
    print("Número ingresado impar")
'''

valor = input("Ingresar el año: ")
anno = int(valor)
if 1990 <= anno < 2000  :
    print("Decada de los 90's")

elif 2000 <= anno < 2010 :
    print("Decada de los 2000's")

else:
    print("Decada actual")