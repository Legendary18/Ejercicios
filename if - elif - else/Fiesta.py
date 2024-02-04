#quienes pueden ir a la fiesta y quienes no, solo pueden ir los mayores de edad

Edad = int(input("Ingrese su edad: "))

if Edad > 50:
    print("Eres una persona de tercera edad.")
elif 45 <= Edad <= 50:
    print("Eres un adulto mayor.")
elif Edad >= 18:
    print("Puedes ir a la fiesta.")
else:
    print("No puedes ir a la fiesta.")
