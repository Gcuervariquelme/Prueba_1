
def encontrar_palabras_comunes(lista1, lista2):
    # Convierte las listas en conjuntos
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Encuentra las palabras comunes
    palabras_comunes = set1.intersection(set2)
    
    # Convierte el conjunto de palabras comunes en una lista
    lista_comunes = list(palabras_comunes)
    
    return lista_comunes

# Ejemplo de uso
def encontrar_palabras_comunes(lista1, lista2):
    # Convierte las listas en conjuntos
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Encuentra las palabras comunes
    palabras_comunes = set1.intersection(set2)
    
    # Convierte el conjunto de palabras comunes en una lista
    lista_comunes = list(palabras_comunes)
    
    return lista_comunes

lista1 = input("Ingresa la primera lista de palabras separadas por espacios: ").split()
lista2 = input("Ingresa la segunda lista de palabras separadas por espacios: ").split()

palabras_comunes = encontrar_palabras_comunes(lista1, lista2)
print("Palabras comunes:", palabras_comunes)


