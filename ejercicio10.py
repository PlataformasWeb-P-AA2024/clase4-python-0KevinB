archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()

print(len(lineas))

lineas = [l.split("|") for l in lineas]

# El archivo 0 son las cabeceras 
for i, x in enumerate(lineas, 0):
    cadena = """
            <b>Torneo:</b> %s <br> <b> Ganador: </br> %s
            """ % (x[0], x[9])
    with open("data/%s.html" % i, "w") as archivo_generado:
        archivo_generado.write("%s\n" % cadena)
