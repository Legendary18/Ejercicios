#El usurio tine que ingresar un numero y puede repetir cuantas veces requiera

Numero = (input("Ingresa el numero que desee repetir "))
veces = int(input("¿Cuantas veces quiere repetir? "))

for _ in range (veces):
    print (Numero)
    