# Importamos la función cargar_registros desde archivo.py para poder acceder a los registros guardados en el archivo de texto
from archivo import cargar_registros

# Llama a la función cargar_registros para obtener la lista de registros
# y luego los ordena por el campo "codigo_sunat" usando el algoritmo de burbuja.
# Finalmente, imprime los registros ordenados en un formato legible.
def listar_ordenado():
    registros = cargar_registros()

    if not registros:
        print("No hay guías registradas todavía.")
        return
# --- INICIO DEL ALGORITMO DE LA BURBUJA (Bubble Sort) ---
    n = len(registros)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if registros[j]["codigo_sunat"] > registros[j + 1]["codigo_sunat"]:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]
                
    #impreme los registros ordenados en un formato legible
    print("\n--- Guías ordenadas por código SUNAT ---")
    for r in registros:
        print(f"{r['codigo_sunat']} | {r['fecha']} | Proveedor: {r['ruc_proveedor']} | {r['items']} ({r['cantidades']})")