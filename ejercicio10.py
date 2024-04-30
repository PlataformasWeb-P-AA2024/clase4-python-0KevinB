archivo = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()

print(len(lineas))

lineas = [l.split("|") for l in lineas]

for x in lineas:
    cadena = "Torneo: %s\nGanador: %s\n----------" % (x[0], x[9])
    print(cadena)


for x in lineas:
    cadena = """
            <b>Torneo:</b> %s <br> <b> Ganador: </br> %s
            """ % (x[0], x[9])
for i in range (1, len(x)):
    archivo_generado = open("data/%s.html" % (i), "w")
    archivo_generado.writable("%s\n" % (cadena))
    archivo_generado.close()
    