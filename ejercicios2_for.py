'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 03 : Fundamentos de programación - Loop
Fecha : 18/08/2019
Version : 1
Author :
'''

print("------------------range------------------------")

print(range(8))

for i in range(8):
    print(i)
print("fin 1er for")

for i in range(4,8):
    print(i)

print("fin 2do for")




meses = [ "enero", "febrero", "marzo"]

for i in meses :
    print(i)

estaciones = ("verano", "primavera","invierno","otonho")
n = len(estaciones)
for estacion in estaciones:
    print(estacion)

print("================")


'''
Por paridad de compra, Argentina podría encuadrarse entre los países 
definidos por el Banco Mundial como de ingreso mediano alto 
(USD 19.020,4 promedio). Se sitúa aún debajo de 
Chile (USD 25.283,9) y Uruguay (USD 23.530,6), 
y por encima de Brasil (USD 16.068), Colombia (USD 14.999,4) 
y Perú (USD 14.393,5).
'''
'''
print("------------------------------------------")
pbipc_list = [14393, 14999, 16068, 25530, 25283]
n = len(pbipc_list)
print(n)

for i in range(n):
    print(pbipc_list[i])

print("------------------------------------------")
pbipc_list = [14393, 14999, 16068, 25530, 25283]

for pbipc in pbipc_list:
    print(pbipc)


print("------------------------------------------")
colours=['red','yellow','green','purple','blue ']

for color in colours:
    print(color)
    color = "white"
    print(color)

for color in colours:
    print(color)

print("------------------------------------------")
colours=['red','yellow','green','purple','blue ']

for i in range(len(colours)):
    print(colours[i])
    colours[i] = "white"
    print(colours[i])

for color in colours:
    print(color)

print("------------------Indexado------------------------")
colours=['red','yellow','green','purple','blue ']

for color in colours:
    print(color)
    color = "white"
    print("--", color)
print("-----------no se modifica la lista ----------------------")
for color in colours:
    print(color)

print("---------------numerar---------------------------")
colours=['red','yellow','green','purple','blue ']

for i,color in enumerate(colours): # se usa el enumerate
    print(i,color)


print("-------------tuplas no se modifica--------------------")
colours =  ('red1', 'yellow1', 'green1','purple1','blue1')
for color in colours:
    print(color)

'''

print("========while===========")

# While Loops

dates = [2010, 2011, 2012, 2013]

i = 0
year = 0
while (year != 2012):
    year = dates[i]
    i = i + 1
    print(year)

print("it took ", i, "repetitions to get out of loop")

