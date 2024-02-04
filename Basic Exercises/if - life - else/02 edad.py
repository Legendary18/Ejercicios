Edad = int(input("Imgresa la tu edad "))

if Edad <= 13:
    print("Eres un niño ")
elif 13 <= Edad < 18:
    print("Eres adolescente ")
elif Edad ==60 or Edad > 61:
    print ("Es un adulto Mayor ")
else:
    print ("Eres un adulto ")