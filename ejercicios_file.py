'''
Programa : Ciencia de Datos con Pthon
Modulo 01 : Fundamentos de Python para Ciencia de Datos
Sesion 03 : Fundamentos de programación - Archivos
Fecha : 21/07/2019
Version : 1
Author :
'''
'''
archivo = open("datos.txt","r")
print(type(archivo))
print(archivo.name)
print(archivo.mode)
datos = archivo.read()
print(type(datos)) # valores stream
print(datos)
archivo.close()


def lectura(nombre_archivo) :
    archivo = open(nombre_archivo,"r")
    datos = archivo.read()
    archivo.close()
    return datos


nombre_archivo = input("ingresar nombre de archivo con extension: ")
info = lectura(nombre_archivo)
print(info)

nombre_archivo =  "C:\\Deportes\\Enero.txt" # Se coloca doble back \\ para bloquear caracter de control
infor = lectura(nombre_archivo)
print(infor)

print("es una \\ lines \n es \t\t\t\t\totro\t linea, \n nuevamente")


print("=======otra forma de leer==========")

with open("datos.txt","r") as archivo:
    contenido = archivo.read()
    print(contenido)

try :
    print(lectura("datos123.txt")) # Funcion
except FileNotFoundError as e:
    print(e.strerror)
    print("Archivo no encontrado")


with open("datos.txt","r") as archivo:
    print(archivo.read(4))
    print(archivo.read(4))
    print(archivo.read(4))
    print(archivo.read(4))  # el print lanza salto de linea

'''

print("=======Escribir por linea===========")
#Si no existe el archivo lo creas

with open("mensajes.txt","w") as archivo:
    archivo.write("Es el primer mensaje\n")

with open("mensajes.txt","a") as archivo: # a : agrega linea
    archivo.write("Es el segundo mensaje\n")

with open("mensajes.txt","a") as archivo:
    archivo.write("Es el tercero mensaje\n")

print("=======Copiar archivo===========")
with open("mensajes.txt","r") as archivo_origen:
    with open("mensajes.txt", "r") as archivo_origen:
##falta completar
