from archivo import cargar_registros

def listar_ordenado():
    registros = cargar_registros()

    if not registros:
        print("No hay guías registradas todavía.")
        return

    n = len(registros)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if registros[j]["codigo_sunat"] > registros[j + 1]["codigo_sunat"]:
                registros[j], registros[j + 1] = registros[j + 1], registros[j]

    print("\n--- Guías ordenadas por código SUNAT ---")
    for r in registros:
        print(f"{r['codigo_sunat']} | {r['fecha']} | Proveedor: {r['ruc_proveedor']} | {r['items']} ({r['cantidades']})")