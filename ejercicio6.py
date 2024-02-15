def separar_personajes():
    humanos = []
    no_humanos = []

    for _ in range(10):
        personaje = input("Ingrese el nombre de un personaje de videojuego: ")
        tipo = input("¿Es humano o no humano? (h/n): ")

        if tipo.lower() == "h":
            humanos.append(personaje)
        elif tipo.lower() == "n":
            no_humanos.append(personaje)
        else:
            print("Tipo de personaje inválido. Se omitirá.")

    humanos = sorted(humanos)
    no_humanos = sorted(no_humanos)

    return humanos, no_humanos

# Ejemplo de uso
personajes_humanos, personajes_no_humanos = separar_personajes()
print("Personajes humanos:", personajes_humanos)
print("Personajes no humanos:", personajes_no_humanos)
