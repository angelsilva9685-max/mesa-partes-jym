from archivo import cargar_registros


def buscar(codigo):
    registros = cargar_registros()
    for registro in registros:
        if registro["codigo_sunat"] == codigo:
            return registro
    return None