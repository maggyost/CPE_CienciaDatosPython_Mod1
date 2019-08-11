'''
Programa: Ciencia de Datos con Python
Modulo: Fundamentos Python
Sesion 02: Estructura de datos - Listas
Fecha: 04/08/2019
Version: 1
Autor : Magaly Ostos
'''

print ( "======Listas=====")

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019, 199]
print("list1      : ", list1)
print("len(list1) : ", len(list1)) # longitud
print("lists[0]   : ", list1[0])
print("lists[1]   : ", list1[1])
print("lists[2]   : ", list1[2])
print("lists[3]   : ", list1[3])
print("lists[0:2] : ", list1[0:2])  # No incluye list1[2]
print("lists[1:3] : ", list1[1:3])  # No incluye list1[3]

print("-----------------valores negativos---------------------")
list1 = ["Panam Sports", 28.07, 2019, 199]
print("list1      : ", list1)
print("len(list1) : ", len(list1))
print("lists[-4]   : ", list1[-4])
print("lists[-3]   : ", list1[-3])
print("lists[-2]   : ", list1[-2])
print("lists[-1]   : ", list1[-1])

print("--------------------------------------")
list1 = \
    ["Panam Sports", 28.07, 2019, 199, [21, 3.14]]

print("list1      : ", list1)
print("len(list1) : ", len(list1))
print("lists[-5]   : ", list1[-5])
print("lists[-4]   : ", list1[-4])
print("lists[-3]   : ", list1[-3])
print("lists[-2]   : ", list1[-2])
print("lists[-1]   : ", list1[-1])

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019, 199,
         [21, 3.14], (10, 8)]

print("list1      : ", list1)
print("len(list1) : ", len(list1))
print("lists[-6]   : ", list1[-6])
print("lists[-5]   : ", list1[-5])
print("lists[-4]   : ", list1[-4])
print("lists[-3]   : ", list1[-3])
print("lists[-2]   : ", list1[-2])
print("lists[-1]   : ", list1[-1])

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019, 199,
         [21, 3.14], (10, 8)]

print("list1           : ", list1)
print("type(list1)     : ", type(list1))
print("type(lists[-6]) : ", type(list1[-6]))
print("type(lists[-5]) : ", type(list1[-5]))
print("type(lists[-4]) : ", type(list1[-4]))
print("type(lists[-3]) : ", type(list1[-3]))
print("type(lists[-2]) : ", type(list1[-2]))
print("type(lists[-1]) : ", type(list1[-1]))

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019]
print("list1[0] : ", list1[0])
list1[0] = "Olympics" # permite cambios
print("list1[0] : ", list1[0])
print("list1    : ", list1)

'''
print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019]
print("list1[0] : ", list1[0])
list1[3] = "Olympics"
print("list1[3] : ", list1[3])
print("list1    : ", list1)
#'''

print("-------------Borrar-------------------------")
list1 = ["Panam Sports", 28.07, 2019]
print("list1    : ", list1)
print("list1[0] : ", list1[0])
del(list1[0])
print("del(list1[0]) ")
print("list1    : ", list1)

print("-----------------append---------------------")

list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)
list1.append(["Rugby", 11])  # agrega el elemento tal cual indica el append
print("list1.append()  : ", list1)


print("--------------extend------------------------")

list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)
list1.extend(["Rugby", 11]) # extiende la lista
print("list1.extend()  : ", list1)


print("------------------Suma de Listas--------------------")
#Es como el extend
#Hace más procesos
list1 = ["Panam Sports", 28.07, 2019]
list2 = ["Rugby", 11]
list1 = list1 + list2
print("list1 + list2  : ", list1)

print("------------------Ejemplo Tuplas--------------------")

tupla_e1 = (1,2,3)
tupla_e2 = (4,5,6)
tupla_s = tupla_e1 + tupla_e2
print(tupla_s)
#Tupla se define en un bloque de memoria
#Como list se crean en espacio de memoria y el extend o append buscan espacion en memoria
list_e1 = [1,2,3]
list_e2 = [4,5,6]
list_e = list_e1 + list_e2
list_e3 = list_e1.extend(list_e2)
print()
#Una tupla de 1 elemento se define (Valor,) caso contrario se lee como valor
tupla_e5 = (5,)
print(tupla_e5)
print(type(tupla_e5))

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)
list1.append(("Rugby", 11))
print("list1.append()  : ", list1)


print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019]
print("list1           : ", list1)
list1.extend(("Rugby", 11))
print("list1.extend()  : ", list1)

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019]
list2 = [("Rugby", 11), 4, 5]
print("list1                : ", list1)
print("list2                : ", list2)
list1.append(list2)
print("list1.append(list2)  : ", list1)

print("--------------------------------------")
list1 = ["Panam Sports", 28.07, 2019]
list2 = [("Rugby", 11), 4, 5]
print("list1                : ", list1)
print("list2                : ", list2)
list1.extend(list2)
print("list1.extend(list2)  : ", list1)


print("============Dividir=================")

print("--------------------------------------")
msg = "Panam Sports - Lima Peru"
print("msg         :", msg)
print("msg.split() :", msg.split()) # hace caso a espacio en blanco

print("--------------------------------------")
abc = "A,B,C,D,E,F,G"
abcList = abc.split(",")  # esta dividiendo por ,
print("abc             :", abc)
print("abc.split(\",\")  :", abcList)

lista_cadena = ['A','B']

print("----------ejemplo split----------------------------")
#================
str_1 = "1:2:3:4:5"
str_2 = str_1.split(":")
print(str_2)
tupla_e3 = tuple(str_2)
print(tupla_e3)
list_e1 = list(tupla_e3)
print(list_e1)
print()
#================
list_e6 = list(tuple(str_1.split(":")))
print(list_e6)

print("============DEL===========")
list_ee1 = [1,2,3,4]
list_ee2 = list_ee1
list_ee3 = [5,6]
list_ee1 = list_ee1.extend(list_ee3)
print(list_ee1)
print(list_ee2)
#del(list2[2])
x1 = 4  # Valores no puntero de lista
x2 = x1
x1 = 3

print(x2)

print("============Ejemplo===========")
#Definir número de una lista de los sigtes elementos
list_x = [1,2,3,4,5,6]
#Eliminar numero pares y luego mostras lista con numero pares y otra con valores impares
list_y = list_x.copy()
print(list_y)
list_z = list_x.copy()
print(list_z)
del(list_y[2])
del(list_y[0])
print(list_y)
del(list_z[3])
del(list_z[1])
print(list_z)

list_a = print(list_x[0:3:2])
list_b = print(list_x[1::2])

print("==========Ordenar========")

valores = [2,8,1,10,-3]
valores_1 = sorted(valores) # aqui hace copia
valores.sort() # ordena la misma lista

print (valores)
print (valores_1)
print("==========Ordenar y Sumar========")
numeros = [1,3,2,5,4,8,6,9,7,0]
#suma de pares y impares
numeros.sort()
print(numeros)
pares = numeros[0::2]
print(pares)
impares = numeros[1::2]
print(impares)
suma_par = sum(pares)
#suma_par1 = pares[0]+pares[1]+pares[2]+pares[3]+pares[4]
print(suma_par)
suma_impar = sum(impares)
#suma_impar1 = impares[0]+impares[1]+impares[2]+impares[3]+impares[4]
print(suma_impar)

print("================Existencias en Listas==================")
#Respuestas en booleanos
nombres = ["Jaime","Jose","Juan"]
ExisteJorge = "Jorge" in nombres
print(ExisteJorge)
ExisteJaime = "Jaime" in nombres
print(ExisteJaime)
NoExisteJuan = "Juan" not in nombres
print(NoExisteJuan)



