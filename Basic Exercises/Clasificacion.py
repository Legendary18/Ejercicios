#En una fiesta solo pueden entrar los mayores de edad
#Relizar un programa en la cula clasifique los que pueden entrar y los que no pueden

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if (0<edad):
    print("El numero que ingrso es negativo: ")
elif (edad>=18):
    print("Es mayor de edad")
else:
    print("Es menor de edad")

