def menu_principal():
    while True:
        print("Elija una estructura de datos:")
        print("1. Listas")
        print("2. Tuplas")
        print("3. Diccionarios")
        print("4. Conjuntos")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == '1':
            ejemplo_listas()
        elif opcion == '2':
            ejemplo_tuplas()
        elif opcion == '3':
            ejemplo_diccionarios()
        elif opcion == '4':
            ejemplo_conjuntos()
        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

def ejemplo_listas():
    # Ejemplo de lista
    mi_lista = [1, 2, 3, 4, 5]
    print("Ejemplo de Lista:")
    print("mi_lista = [1, 2, 3, 4, 5]")
    print("mi_lista:", mi_lista)
    print("Elemento en la posición 2:", mi_lista[1])
    print("Longitud de la lista:", len(mi_lista))

def ejemplo_tuplas():
    # Ejemplo de tupla
    mi_tupla = (1, 2, 3, 4, 5)
    print("Ejemplo de Tupla:")
    print("mi_tupla = (1, 2, 3, 4, 5)")
    print("mi_tupla:", mi_tupla)
    print("Elemento en la posición 3:", mi_tupla[2])

def ejemplo_diccionarios():
    # Ejemplo de diccionario
    mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemploville'}
    print("Ejemplo de Diccionario:")
    print("mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemploville'}")
    print("mi_diccionario:", mi_diccionario)
    print("Edad de la persona:", mi_diccionario['edad'])

def ejemplo_conjuntos():
    # Ejemplo de conjunto
    mi_conjunto = {1, 2, 3, 4, 5}
    print("Ejemplo de Conjunto:")
    print("mi_conjunto = {1, 2, 3, 4, 5}")
    print("mi_conjunto:", mi_conjunto)
    otro_conjunto = {3, 4, 5, 6, 7}
    print("Otro conjunto:", otro_conjunto)
    union = mi_conjunto.union(otro_conjunto)
    print("Unión de conjuntos:", union)
    interseccion = mi_conjunto.intersection(otro_conjunto)
    print("Intersección de conjuntos:", interseccion)

if __name__ == "__main":
    menu_principal()
