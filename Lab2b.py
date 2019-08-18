print("======Funcion de Suma de N=====For==== ")

def sum_for(n):
    i = 1
    suma = 0
    LIMITE = n
    while i != LIMITE + 1 :
        suma = suma + i
        i = i + 1
    return suma

print("======Uso de Funcion==== ")

n = int(input("Ingrese en valor n, entero: "))
resultado1 = sum_for(n)

print ( resultado1)