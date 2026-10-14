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
    SEPARADOR = "|"
    for campo, valor in datos.items():
        if not valor:
            print(f"El campo {campo} no puede estar vacio.")
            return False

        if SEPARADOR in valor:
            print(f"El campo {campo} contiene un separador no permitido.")
            return False

    for campo in ("ruc_cliente", "ruc_proveedor"):
        ruc = datos[campo]

        if not ruc.isdigit() or len(ruc) != 11:
            print(f"El campo {campo} debe tener 11 digitos.")
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

