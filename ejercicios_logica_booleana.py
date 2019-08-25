
import numpy as np
print("------------------------------------")
a_matriz = np.random.random((4,4))
print(a_matriz)

#print(np.round(1.335,decimals=2))

a_m = np.apply_along_axis(np.round, axis=1, arr=a_matriz, decimals=2)
print("genera matriz", a_m)

# Se muestran la tabla booleana
print( a_m < 0.5)

# Solo se muestran los que cumplen la condicion
print( a_m[a_m < 0.5])

