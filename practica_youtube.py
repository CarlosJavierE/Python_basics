# nombre = input('Escriba un nombre: ')
mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }


# lista = [54, 5, 564, 54, 54, 5587, 92, 1, 5]

# simplemente se puede poner el diccionario e imprime las claves
# for clave, valor in mi_diccionario():
#     print(clave)

# para obtener los valores
for valor in mi_diccionario.values():
    print(valor)

# se debe colocar 2 variables para hacer el metodo
for clave, valor in mi_diccionario.items():
    print(clave, valor)