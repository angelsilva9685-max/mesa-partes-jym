from archivo import guardar_registro, cargar_registros, CAMPOS


def registrar():
    while True:
        datos = {}
        for campo in CAMPOS:
            datos[campo] = input(f"Ingrese {campo}: ").strip()

        if validar(datos):
            guardar_registro(datos)
            print("Guía registrada con éxito.")
            break
        else:
            print("Datos inválidos, intente nuevamente.")


def validar(datos):
    if not (datos["ruc_cliente"].isdigit() and len(datos["ruc_cliente"]) == 11):
        print("El RUC del cliente debe tener 11 dígitos.")
        return False
    if not (datos["ruc_proveedor"].isdigit() and len(datos["ruc_proveedor"]) == 11):
        print("El RUC del proveedor debe tener 11 dígitos.")
        return False
    try:
        cantidad = float(datos["cantidades"])
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return False
    except ValueError:
        print("La cantidad debe ser un número.")
        return False

    registros = cargar_registros()
    for r in registros:
        if r["codigo_sunat"] == datos["codigo_sunat"]:
            print("Ese código SUNAT ya está registrado.")
            return False
    return True
