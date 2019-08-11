'''
Programa: Ciencia de Datos con Python
Modulo: Fundamentos Python
Sesion 02: Estructura de datos - Sets
Fecha: 11/08/2019
Version: 1
Autor : Magaly Ostos
'''

print("================stes===============")
colourSet = {"red", "green","yellow","blue","blue","blue"}
colourList = ["red", "green","yellow","blue","blue","blue"]
print("colourSet    :  " , colourSet)
#No se aceptan valores repetidos,
#No tiene posición definido
print("colourList    :  " , colourList)
#Se aceptan valores repetidos,
#Si tiene posición definida

print("-------------------agregar y borrar-------------------")
colours = {"red", "green", "yellow", "blue"}
print("colours                :",  colours)
print("len(colours)           :",  len(colours))
print("type(colours)          :",  type(colours))
colours.add("white")
print("colours                :",  colours)
colours.add("white")
print("colours                :",  colours)
colours.remove("green")  # Se borra por el valor que tiene el set
#No se podrá borrar por el INDEX pues no es un index definido
print("colours                :",  colours)

print("--------------------------------------")
colours = {"red", "green", "yellow", "blue"}
print("colours                         :",
      colours)
print("sorted(colours)                 :",
      sorted(colours))
print("sorted(colours, reverse = True) :",
      sorted(colours, reverse = True))

print("---------min,max,suma-----------------------------")
ratings = {0,3,4,19,5,6,7,8}
print("ratings       :", ratings)
print("min(ratings)  :", min(ratings))
print("max(ratings)  :", max(ratings))
print("sum(ratings)  :", sum(ratings))

print("----------------copy----------------------")
set1 = {"Panam Sports", 28.07, 2019}
set2 = set1.copy()
#set2 = set1.{:} --> No se maneja esto en sets
print("set1 :", set1)
print("set2 :", set2)

print("-----------------Union---------------------")
colours1 = {"red", "green", "yellow", "blue"}
colours2 = {"white", "black", "purple"}
print("colours1 :", colours1)
print("colours2 :", colours2)
#colours1 = colours1 + colours2 -->falla tampoco append ni extend
colours1.update(colours2)
print("colours1 :", colours1)

print("=======Ejemplo=======")
num1 = {"uno","dos","tres"}
num2 = {"tres","cuatro","cinco"}
num1.update(num2)
print(num1) # ningun orden en la salida de los valores

print("=======Cambiar a lista=======")
#Aqui quiero valos ocmo lista con todos los elementos
num1 = {"uno","dos","tres"}
num2 = {"tres","cuatro","cinco"}
list_num1 = list(num1)
list_num2 = list(num2)
list_Total = list_num1 + list_num2
print(list_Total)

print("=======AgregarUnValor=======")

num1.add("cien") #Solo se agrega valor
print(num1)

print("=======Eliminar=======")

num1.remove("cien")
print(num1)

print("--------------------------------------")
sportsA = {"Soccer","Tennis","Baseball","Squash"}
sportsB = {"Soccer","Tennis","Rugby","Judo"}
print("sportsA                       :",sportsA)
print("sportsB                       :",sportsB)
print("sportsA & sportsB             :", sportsA & sportsB)
print("sportsA.intersection(sportsB) :", sportsA.intersection(sportsB))
print("sportsA | sportsB             :",sportsA | sportsB)
print("sportsA.union(sportsB)        :",sportsA.union(sportsB))
print("sportsA.difference(sportsB)   :",sportsA.difference(sportsB))
print("sportsB.difference(sportsA)   :",sportsB.difference(sportsA))
print("sportsA ^ sportsB             :",sportsA ^ sportsB)

print("--------Ejemplo-------------------")
nros_a  = {"uno","dos","tres"}
nros_b = {"tres","cuatro","cinco"}
print(nros_a)
print(nros_b)
x = nros_a.union(nros_b)
print(x)
print(nros_a)
y = nros_a.update(nros_b) # No obtiene resultado afecta a nros_a
print(y)
print(nros_a)


