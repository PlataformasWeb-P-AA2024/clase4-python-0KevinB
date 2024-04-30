nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo: "))

mensaje = "Nombre: %s\nEdad: %d\nSueldo: %.2f" % (nombre, edad, sueldo)

print(mensaje)