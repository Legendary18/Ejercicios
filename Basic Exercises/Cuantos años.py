#En el bar solo pueden entrar las personas que son mayores de edad y los que son menores de edad van al parque de diversiones
name = (input("Ingresa tu nombre "))
Bar = int(input("Ingresa tu edad "))
 
if Bar >= 18:
    print ("eres mayor de edad puedes pasar")
   
elif Bar >= 60:
    print ("perteneces a las persona de tercera edad")

else:
    print ("no puedes pasar, eres menor de edad ")

