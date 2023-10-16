def gestionar_agenda():
    agenda = {}

    while True:
        print("Gestión de Agenda de Contactos")
        print("1. Agregar un contacto")
        print("2. Buscar un contacto")
        print("3. Ver todos los contactos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            agenda[nombre] = telefono
            print(f"El contacto {nombre} ha sido agregado a la agenda con el número {telefono}.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto que desea buscar: ")
            if nombre in agenda:
                print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
            else:
                print(f"{nombre} no se encuentra en la agenda.")
        elif opcion == '3':
            if not agenda:
                print("La agenda de contactos está vacía.")
            else:
                print("Agenda de Contactos:")
                for nombre, telefono in agenda.items():
                    print(f"Nombre: {nombre}, Teléfono: {telefono}")
        elif opcion == '4':
            print("Gestión de agenda finalizada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    gestionar_agenda()
