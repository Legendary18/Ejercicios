Edad = int(input("Ingrese su edad "))

if Edad <= 12:
    print("Es un niño")
elif 13 <= Edad < 18:
    print("Es un adolescente")
elif Edad == 60 or Edad >=61:
    print ("Es un adulto mayor")
else:
    print ("Es un adulto ")

