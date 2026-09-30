from registrar import registrar
from buscar import buscar
from ordenar import listar_ordenado

def mostrar_menu():
    print("\n1. Registrar guía")
    print("2. Buscar guía")
    print("3. Listar / Ordenar guías")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            registrar()
        elif opcion == "2":
            codigo = input("Código SUNAT: ").strip()
            resultado = buscar(codigo)
            print(resultado if resultado else "No encontrado")
        elif opcion == "3":
            listar_ordenado()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()