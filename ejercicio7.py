from typing import List
def agregar_item(inventario: List[str], item: str) -> List[str]:
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    inventario.append(item)
    return inventario

# Ejemplo de uso
inventario = ["maletero", "puerta", "motor"]
try:
    agregar_item(inventario, "maletero")
    print(inventario)
    agregar_item(inventario, "rueda")
except ValueError as e:
    print(e)

