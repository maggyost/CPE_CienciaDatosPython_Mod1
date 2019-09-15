import pandas as pd
import matplotlib.pyplot as plt


print("---------------------------------")
archivo_csv = "WEO_Data.csv"
df = pd.read_csv(archivo_csv, thousands=',', decimal='.')
df.rename(columns={'Country': 'Pais'}, inplace=True)
df.set_index('Pais', inplace=True)
America = ['Brazil','Mexico','Argentina','Chile','Peru']
data = df.loc[America,'2019']

df = pd.DataFrame(data)
print(df['2019'])
#print(df['Pais'])
colores = ['green', 'red', 'blue', 'purple', 'yellow']
explode = [0, 0, 0, 0, 0.3]
font = {'family': 'serif',
            'color': 'black',
            'weight': 'normal',
            'size': 16,
        }
#df['2019'].plot(kind='pie', colors=colores)
df['2019'].plot(kind='pie',colors= colores, explode=explode,
                       shadow=True,autopct='%1.2f%%', startangle=180)
plt.title('Latino America - PBI ',fontdict=font)
plt.legend(loc = 'lower right')
plt.ylabel("")
plt.show()
