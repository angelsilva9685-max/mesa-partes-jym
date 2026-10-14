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
    # 1. Validar que no haya campos vacíos y que no usen el separador "|"
    for campo, valor in datos.items():
        if not valor:
            print(f"El campo {campo} no puede estar vacío.")
            return False
        if SEPARADOR in valor:
            print(f"El campo {campo} no puede contener el carácter '{SEPARADOR}'.")
            return False

    # 2. Validar que ambos RUCs tengan 11 dígitos y sean solo números
    for tipo_ruc in ["ruc_cliente", "ruc_proveedor"]:
        if not (datos[tipo_ruc].isdigit() and len(datos[tipo_ruc]) == 11):
            print(f"El {tipo_ruc.replace('_', ' ').title()} debe tener 11 dígitos.")
            return False

    # 3. Validar que la cantidad sea un número mayor a 0
    try:
        cantidad = float(datos["cantidades"])
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return False
    except ValueError:
        print("La cantidad debe ser un número válido.")
        return False

    # 4. Validar que el código SUNAT no esté repetido
    registros = cargar_registros()
    if any(registro["codigo_sunat"] == datos["codigo_sunat"] for registro in registros):
        print("Ese código SUNAT ya está registrado.")
        return False

    return True

