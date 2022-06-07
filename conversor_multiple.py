pesos = float(input("Los pesos que desea convertir: "))
valor_dolar = 6.96
valor_euro = 7.22
valor_yen = 0.053
valor_real = 1.38

# Calculo de dolares
dolares = pesos / valor_dolar
dolares = str(round(dolares, 3))

#Calculo de euros
euros = pesos / valor_euro
euros = str(round(euros, 3))

#Calculo de yenes
yenes = pesos / valor_yen
yenes = str(round(yenes, 3))

#Calculo de reales
reales = pesos / valor_real
reales = str(round(reales, 3))

# Resultados
print("Usted tiene " + dolares + " dolares")
print("Usted tiene " + euros + " euros")
print("Usted tiene " + yenes + " yenes")
print("Usted tiene " + reales + " reales")