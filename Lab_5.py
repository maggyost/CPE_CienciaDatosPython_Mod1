import pandas as pd
import matplotlib.pyplot as plt


print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
data = df['2019']
data = data.sort_values(ascending=False)
data_top10 = data.head(10) # data de los 10 paises
data_top10 = pd.DataFrame(data_top10)
print(type(data_top10))
font = {'family': 'serif',
            'color': 'black',
            'weight': 'normal',
            'size': 16,
        }
data_top10.plot(kind='box')
plt.title('Top Ten Países - PBI ',fontdict=font)
plt.show()

if __name__ == '__main__':
    #basico_box_plot()
    #basico_box_plot_2()
    intermedio_box_plot()