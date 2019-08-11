'''
Programa: Ciencia de Datos con Python
Modulo: Fundamentos Python
Sesion 02: Estructura de datos - Diccionarios
Fecha: 11/08/2019
Version: 1
Autor : Magaly Ostos
'''

print("--------------------------------------")
dict1 = {"key1":"value1", "key2":"value2",
         "key3":"value3"}
print("dict1           :",  dict1)
print("len(dict1)      :",  len(dict1))
print("dict1[\"key1\"] :",  dict1["key1"])
print("dict1[\"key2\"] :",  dict1["key2"])
print("dict1[\"key3\"] :",  dict1["key3"])
print("dict1.keys()    :",  dict1.keys())
print("dict1.values()  :",  dict1.values())

medallas_pe = {"oro":11,"plata":7,"bronce":19}
print("Medallas de Oro", medallas_pe["oro"])
print("Medallas de Plata", medallas_pe["plata"])
print("Medallas de Bronce", medallas_pe["bronce"])
print(medallas_pe.keys())
print(medallas_pe.values())
medallas_pe.update({"oro":12})
print(medallas_pe["oro"])
medallas_pe.update({"total":37})
print(medallas_pe.keys())

print("--------------------------------------")
medalTable_PAG_20190802 \
                 = {"USA":{"Gold":36,"Silver":28,"Bronze":25},
                    "MEX":{"Gold":16,"Silver":11,"Bronze":26},
                    "CAN":{"Gold":14,"Silver":26,"Bronze":18},
                    "BRA":{"Gold":13,"Silver":12,"Bronze":23},
                    "CUB":{"Gold":10,"Silver":10,"Bronze": 9},
                    "ARG":{"Gold":10,"Silver": 7,"Bronze":11},
                    "COL":{"Gold": 8,"Silver": 9,"Bronze":12},
                    "DOM":{"Gold": 4,"Silver": 6,"Bronze": 9},
                    "PER":{"Gold": 4,"Silver": 2,"Bronze": 6},
                    "CHI":{"Gold": 3,"Silver": 5,"Bronze": 5}}

print("medalTable_PAG_20190802                  :", medalTable_PAG_20190802)
print("medalTable_PAG_20190802[\"USA\"]           :", medalTable_PAG_20190802["USA"])
print("medalTable_PAG_20190802[\"BRA\"]           :", medalTable_PAG_20190802["BRA"])
print("medalTable_PAG_20190802[\"PER\"]           :", medalTable_PAG_20190802["PER"])
print("medalTable_PAG_20190802[\"BRA\"][\"Bronze\"] :", medalTable_PAG_20190802["BRA"]["Bronze"])
print("medalTable_PAG_20190802[\"BRA\"][\"Silver\"] :", medalTable_PAG_20190802["BRA"]["Silver"])
print("medalTable_PAG_20190802[\"PER\"][\"Gold\"]   :", medalTable_PAG_20190802["PER"]["Gold"])
