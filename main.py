# Importamos las funciones principales desde los otros archivos
from registrar import registrar
from buscar import buscar
from ordenar import listar_ordenado

# Esta función sirve únicamente para imprimir en pantalla las opciones del menú
def mostrar_menu():
    print("\n1. Registrar guía")
    print("2. Buscar guía")
    print("3. Listar / Ordenar guías")
    print("4. Salir")

# Función principal. Controla el flujo y nunca se detiene sola.
def main():
    while True:
        mostrar_menu() # Llama a la función de arriba para mostrar el texto en pantalla
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

# Llave de encendido: Asegura que el programa solo inicie desde main.py
if __name__ == "__main__":
    main()