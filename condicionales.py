# edad = int(input("escribe tu edad: "))
# if edad > 17:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

# numero = int(input("Escribe un numero: "))
# if numero > 5:
#     print("Es mayor a 5")
# elif numero == 5:
#     print("Es igual a 5")
# else:
#     print("Es menor a 5")

nacionalidad = input("¿Eres peruano? (Responde sí o no) ")
if nacionalidad == "sí":
    cambio_a_soles = 3.9865
    dolares = str(round(float(input("¿Cuántos soles tienes? "))/cambio_a_soles, 2))
    print("Entonces tienes " + dolares + " dólares.")
elif nacionalidad == "no":
    cambio_a_dolares = 0.25298
    soles = str(round(float(input("Bienvenido a Perú. ¿Cuántos dólares tienes? "))/cambio_a_dolares, 2))
    print("Entonces tienes " + soles + " soles.")
else:
    print("Escribe sólo sí o no, por favor. ")