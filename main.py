def ingresar_suscriptores(suscriptores: set) -> None:
    n = int(input('Cantidad de suscriptores a ingresar: '))
    for _ in range(n):
        email = input('Nuevo suscriptor (email): ').strip()
        suscriptores.add(email)

def agregar_suscriptor(suscriptores: set) -> None:
    email = input('Email nuevo suscriptor: ').strip()
    if email in suscriptores:
        print(f'El suscriptor "{email}" ya existe.')
    else:
        suscriptores.add(email)
        print(f'Suscriptor "{email}" agregado.')

def eliminar_suscriptor(suscriptores: set) -> None:
    email = input('Email a eliminar: ').strip()
    if email in suscriptores:
        suscriptores.remove(email)
        print(f'Suscriptor "{email}" eliminado.')
    else:
        print(f'"{email}" no está en la lista.')

def mostrar_suscriptores(suscriptores: set) -> None:
    print(f'\nTotal: {len(suscriptores)} suscriptores')
    for s in sorted(suscriptores):
        print(f'- {s}')

def main():
    suscriptores = set()
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar suscriptores")
        print("2. Agregar uno")
        print("3. Eliminar uno")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ingresar_suscriptores(suscriptores)
        elif opcion == "2":
            agregar_suscriptor(suscriptores)
        elif opcion == "3":
            eliminar_suscriptor(suscriptores)
        elif opcion == "4":
            mostrar_suscriptores(suscriptores)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
