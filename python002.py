def crear_lista_de_compras():
    lista_de_compras = []

    while True:
        print("Gestión de Lista de Compras")
        print("1. Agregar un artículo a la lista de compras")
        print("2. Ver la lista de compras")
        print("3. Finalizar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            articulo = input("Ingrese el nombre del artículo que desea agregar: ")
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            tupla_articulo = (articulo, cantidad)
            lista_de_compras.append(tupla_articulo)
            print(f"{cantidad} {articulo} ha sido agregado a la lista de compras.")
        elif opcion == '2':
            if not lista_de_compras:
                print("La lista de compras está vacía.")
            else:
                print("Lista de Compras:")
                for item in lista_de_compras:
                    articulo, cantidad = item
                    print(f"- {cantidad} {articulo}")
        elif opcion == '3':
            print("Lista de compras finalizada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    crear_lista_de_compras()
