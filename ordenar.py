import re
from archivo import cargar_registros


def clave_orden(codigo):
    return [(0, int(t), "") if t.isdigit() else (1, 0, t)
            for t in re.findall(r"\d+|\D+", codigo)]


def listar_ordenado():
    registros = cargar_registros()

    if not registros:
        print("No hay guías registradas todavía.")
        return

    n = len(registros)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if clave_orden(registros[j]["codigo_sunat"]) > clave_orden(registros[j + 1]["codigo_sunat"]):
                registros[j], registros[j + 1] = registros[j + 1], registros[j]

    print("\n--- Guías ordenadas por código SUNAT ---")
    for r in registros:
        print(f"{r['codigo_sunat']} | {r['fecha']} | Proveedor: {r['ruc_proveedor']} | {r['items']} ({r['cantidades']})")