'''
Programa: Ciencia de Datos con Python
Modulo: Fundamentos Python
Sesion 02: Estructura de datos - Tuples
Fecha: 04/08/2019
Version: 1
Autor : Magaly Ostos
'''

tuple1=("Smartphone",10,1.2)

print("--------------------------------------")
print(tuple1)
print(type(tuple1))
print("--------------------------------------")
print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print("--------------------------------------")
print(tuple1)
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print("--------------------------------------")
print(tuple1)
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

print("Medallero")

medallero = ("Oro",4,"Plata",3,"Bronce",10)

print(medallero)

print(medallero[0],": ", medallero[1])
print(medallero[2],": ", medallero[3])
print(medallero[4],": ", medallero[5])

print(len(medallero))

msg = "Bienvenido"

#medallero[0] = "Gold" # No permite cambios

msg = "Welcome"

'''
print("--------------------------------------")
tuple1=("Smartphone",10,1.2)
print("tuple1[0] : ", tuple1[0])
tuple1[0] = "Tablet"
print("tuple1[0] : ", tuple1[0])
print("tuple1    : ", tuple1)
#'''

print("--------------Agregar Valores Tuplas------------------------")
tuple1=("Smartphone",10,1.2)
tuple2 = tuple1 + ("tablet",8)
print(tuple2)
print(tuple2[0:3]) # Sale como maximo - 1--> 0 a 2
print(tuple2[3:5]) # 3 y 4
print(len(tuple2))

'''
print("--------------------------------------")
ratings = (0,3,4,19,5,6,7,8)
print("ratings       :", ratings)
ratings.sort()
print("ratings       :", ratings)
ratings = (0,3,4,19,5,6,7,8)
print("ratings       :", ratings)
ratings.sort(reverse=True)
print("ratings       :", ratings)
'''


###
print("===Acceso de Elementos Tuples===")
nestledTuple = (2,4,"Panam Sports", (1,2),
                ("Soccer Game", 4, (5,8)))

print("--------------------------------------")
print("Tuple     :", nestledTuple)
print("element 0 :", nestledTuple[0]) #2
print("element 1 :", nestledTuple[1]) #4
print("element 2 :", nestledTuple[2]) #Panam Sports
print("element 3 :", nestledTuple[3]) #Tupla (1,2)
print("element 4 :", nestledTuple[4]) #Tupla ("Soccer Game", 4, (5,8))

print("--------------------------------------")
print("Tuple         :", nestledTuple)
print("element 0     :", nestledTuple[0])
print("element 2     :", nestledTuple[2])
print("element 2,0   :", nestledTuple[2][0])
print("element 3,1   :", nestledTuple[3][1])
print("element 4     :", nestledTuple[4])
print("element 4,0   :", nestledTuple[4][0])
print("element 4,1   :", nestledTuple[4][1])
print("element 4,2   :", nestledTuple[4][2])
print("element 4,2,0 :", nestledTuple[4][2][0])
print("element 4,0,7 :", nestledTuple[4][0][7])

str = "Magaly Ostos"
tuple3 = tuple(str)
print(tuple3)
print(tuple3[0],".",tuple3[7])


print("---------------Orden de Tuples-----------------------")
ratings = (0,3,4,19,5,6,7,8)
ratingsSorted = sorted(ratings) # se ordena sobre otra variable que sale lista
ratingsReverseSorted = sorted(ratings,reverse=True)  # lista
print(ratings)
print(type(ratings))
print(ratingsSorted)
print(type(ratingsSorted))
ratingsSorted = tuple(ratingsSorted) # Se cambia a Tuple
print(type(ratingsSorted)) # Se cambia a Tuple
print(ratingsReverseSorted)
print(type(ratingsReverseSorted))


print("---------------CloneTuplas-----------------------")
ratings = (0,3,4,19,5,6,7,8)
ratingsClone = ratings
print(ratingsClone)
print(type(ratingsClone)) # sigue siendo tuplas

tuple4 = ("clone","test")
ratingsClone = ratingsClone + tuple4
print(ratings)
print(ratingsClone)

print("--------------------------------------")
ratings = (0,3,4,19,5,6,7,8)
print("ratings       :", ratings)
print("min(ratings)  :", min(ratings))
print("max(ratings)  :", max(ratings))
print("sum(ratings)  :", sum(ratings))

print("----------------Busquedas----------------------")
sports = ("Soccer","Tennis","Baseball","Squash")
print("sports                   :", sports)
#print("sports.index(\"Soccer\")   :",
#     sports.index("Soc"))
print('sports.index("Soccer")   :', sports.index("Soccer")) # Resultado es el indice de la palabra
print("sports.index(\"Baseball\") :", sports.index("Baseball"))
# \ \ esto indica que las "" dentro de comentario se debe considerar.

print("-------------Busqueda-------------------------")
sports = ("Soccer","Tennis","Baseball","Squash")
existShotting = "Shotting" in sports
print("sports                :", sports)
print("existShotting         :", existShotting) #no existe sale false
existSoccer = "Soccer" in sports
print("existSoccer           :", existSoccer) # existe True

print("--------------------------------------")
sports = ("Soccer","Tennis","Baseball","Squash")
notExistShotting = "Shotting" not in sports
print("sports             :", sports)
print("notExistShotting   :", notExistShotting)
notExistSoccer = "Soccer" not in sports
print("notExistSoccer     :", notExistSoccer)

print("--------------------------------------")
samples = (0,3,4,3,5,5,5,5,1,1)
print("samples             :", samples)
print("samples.count(1)    :", samples.count(1))
print("samples.count(3)    :", samples.count(3))
print("samples.count(5)    :", samples.count(5))

print("--------------------------------------")
tuple1=("Smartphone",10,1.2)
for value in tuple1 :
    print(value)

