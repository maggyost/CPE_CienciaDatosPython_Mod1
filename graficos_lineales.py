'''

'''

import matplotlib.pyplot as plt
import numpy as np
#Los valores aislados de las funciones
LIM_INF = -10
LIM_SUP = 10
RAZON = 0.1
x = np.arange(LIM_INF, LIM_SUP, RAZON)
print(x)

def graficos_lineales_1() :

    plt.plot(x,x, label = "linea 1")
    plt.plot(x,4*x+20, label = "linea 2")
    #plt.plot(x, np.sqrt(x))
    plt.plot(x, x*x, label = "linea 3")
    plt.legend()


    plt.xlabel("Valores de X")
    plt.ylabel("Valores de y")
    plt.title("Graficos de Líneas con Python")

    plt.xlim(4,8)
    plt.ylim(40,60)

    plt.show()

    plt.savefig("fig-01")  # no graba bien

def graficos_lineales_2():
    plt.plot(x,np.sin(x), label = "Funcion Seno")
    plt.show()


def graficos_lineales_3():
    plt.plot(x,np.log10(x), label = "Funcion Logaritno 10")
    plt.show()

def graficos_lineales_4():
    plt.plot(x,mi_patron(x), label = "Mi Funcion")
    plt.show()

def mi_patron(x):
  #  modelo = 3*x
    modelo = 3*pow(x,3) + 5*pow(x,2) + 4*x + 4
    modelo = np.log10(x)*modelo
    return modelo

def graficos_lineales_5():
    plt.subplot(2,2,1)
    plt.plot(x,np.sin(x),'.-g')
    plt.subplot(2, 2, 2)
    plt.plot(x, np.cos(x),'m')
    plt.subplot(2, 2, 3)
    plt.plot(x,np.tan(x),'y')
    plt.subplot(2, 2, 4)
    plt.plot(x, 1/np.tan(x), )
    plt.show()


if __name__ == '__main__':
    #graficos_lineales_1()
    #graficos_lineales_2()
    #graficos_lineales_3()
    #graficos_lineales_4()
    graficos_lineales_5()