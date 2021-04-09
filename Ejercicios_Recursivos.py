# Ejercicio 5

def romano_a_decimal(n_romano):
    numero_rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if n_romano == "":
        return 0
    else:
        return numero_rom[n_romano[0]] + romano_a_decimal(n_romano[1:])


print("Su numero romano pasado a decimal es: ", romano_a_decimal("XXVL"))


# Ejercicio 8

def decimal_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_binario(numero // 2) + str(numero % 2)


print("El numero decimal en binario es: ", decimal_binario(2))


# Ejercicio 21

def busqueda_binaria_r(lista, x, izq, der) -> object:
    medio = (izq + der) // 2

    if izq > der:
        return -1
    elif lista[medio] == x:
        return medio + 1
    elif lista[medio] < x:
        return busqueda_binaria_r(lista, x, medio + 1, der)
    else:
        return busqueda_binaria_r(lista, x, izq, medio - 1)


lista_n = [1, 3, 5, 7, 9, 11, 13, 15]
print("El indice de su buscado es: ", busqueda_binaria_r(lista_n, 11, 0, len(lista_n) - 1))


# Ejercicio 22

def usar_la_fuerza(mochila, sable, pos):

    if mochila[pos] == sable:
        return pos + 1
    elif pos == len(mochila) - 1:
        return - 1
    else:
        return usar_la_fuerza(mochila, sable, pos + 1)


mochila = ["Cepillo Jedai", "Reloj Jedai", "Foto de Yoda", "Sable de luz", "Regalo de Padme"]
posicion = (usar_la_fuerza(mochila, "Sable de luz", 0))
if posicion != -1:
    print("Se encontro el Sable de luz en la posición: ", posicion)
    print("Se necesitaron sacar", posicion - 1, "objetos para encontrarlo")