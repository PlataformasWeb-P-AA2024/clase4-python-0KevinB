diccionario = {} 

diccionario["nombre"] = "Kevin Alexander"
diccionario["apellido"] = "Barrazueta Quizhpe"
diccionario["ciudad"] = "Loja"

print(diccionario.keys())
print(diccionario["apellido"])

#Presentar todos los valores de las llaves del diccionario

print(diccionario)

for x in diccionario.keys():
    print(diccionario[x])