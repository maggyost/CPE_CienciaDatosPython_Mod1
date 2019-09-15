import matplotlib.pyplot as plt
import pandas as pd

'''
print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.rename(columns={'Country': 'Pais'}, inplace=True)
'''

# Scatter plots
def basico_scatter():
    ' Ejemplo basico de scatter plot'
    notas_alumnas = [89, 90, 70, 89, 100,
                     80, 90, 100, 80, 34]
    rango_notas   = [10, 20, 30, 40, 50,
                     60, 70,  80, 90, 100]
    plt.scatter(rango_notas, notas_alumnas,
                color='r',label= "Nota de Alumnas")
    plt.title("Notas obtenida por las alumnas")
    plt.xlabel('Rango de Notas')
    plt.ylabel('Nota Asignada')
    plt.savefig("img/scatter-01")
    plt.show()

def intermedio_scatter():
    ' Ejemplo basico de scatter plot'
    notas_alumnas = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    notas_alumnos = [30, 29, 49, 48, 100, 48, 38,  45, 20, 30]
    rango_notas   = [10, 20, 30, 40, 50,  60, 70,  80, 90, 100]
    plt.scatter(rango_notas, notas_alumnas, color='r',label= "Notas de Alumnas")
    plt.scatter(rango_notas, notas_alumnos, color='g',label= "Notas de Alumnos")
    plt.xlabel('Rango de Notas')
    plt.ylabel('Nota Asignada')
    plt.legend()
    plt.savefig("img/scatter-02")
    plt.show()


def dataframe_basico_scatter():
    data = {'Nota de Alumnas': [89, 90, 70, 89, 100, 80, 90, 100, 80, 34],
            'Rango de Notas': [10, 20, 30, 40, 50,  60, 70,  80, 90, 100]}
    df = pd.DataFrame(data)
    df.plot(kind='scatter', x='Rango de Notas', y = "Nota de Alumnas" )
    plt.title("Diagrama de Dispersion")
    plt.ylabel("Notas")
    plt.savefig("img/scatter-06")
    plt.show()




if __name__ == '__main__':
    #basico_scatter()
    #intermedio_scatter()
    dataframe_basico_scatter()