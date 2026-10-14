from archivo import guardar_registro, cargar_registros, CAMPOS, SEPARADOR


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

    except (ValueError, TypeError):
        print("La cantidad debe ser un numero valido.")
        return False

    registros = cargar_registros()
    codigo = datos["codigo_sunat"]

    duplicado = any(
        registro["codigo_sunat"] == codigo
        for registro in registros
    )

    if duplicado:
        print("Ese codigo SUNAT ya esta registrado.")
        return False

    return True

