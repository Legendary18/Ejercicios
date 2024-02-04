print("Programas de Becas 2024")
print("Estos son los requisitos que debe tener para otorgarle una beca")

Distancia = int(input("Ingresa la distancia: "))

Números_de_hermanos = int(input("Ingresa los números de hermanos: "))

Salario_familiar = int(input("Ingresa el salario familiar: "))

promedio = int(input("Ingresa el promedio: "))


if Distancia >= 40 and Números_de_hermanos > 2 and Salario_familiar < 7000 and promedio >= 8:


    print("Tienes beca")
else:
    print("Lo siento, no cumples con los requisitos para la beca.")
    
    if Distancia < 40:
        print("Distancia insuficiente.")
    if Números_de_hermanos <= 2:
        print("Número de hermanos insuficiente.")
    if Salario_familiar >= 7000:
        print("Salario familiar demasiado alto.")
    if promedio < 8:
        print("Promedio insuficiente.")