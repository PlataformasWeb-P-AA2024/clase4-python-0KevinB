nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo: "))

if sueldo <= 100:
    print("correcto")
else:
    print("Incorrecto")



# mensaje = "Nombre: %s\nEdad: %d\nSueldo: %.2f" % (nombre, edad, sueldo)

# print(mensaje)

if sueldo <= 100:
    print("correcto")
else:
    if(sueldo >= 1001 and sueldo <= 1200):
        print("Sobresaliente")
    else: 
        print("Incorrecto")
