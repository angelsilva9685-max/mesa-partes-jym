import os

ARCHIVO = "guias.txt"
SEPARADOR = "|"
CAMPOS = ["codigo_sunat", "ruc_cliente", "ruc_proveedor", "fecha",
          "punto_salida", "punto_llegada", "peso", "items",
          "cantidades", "receptor", "orden_compra", "comprobante"]


def guardar_registro(datos):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        linea = SEPARADOR.join(str(datos[campo]) for campo in CAMPOS)
        f.write(linea + "\n")


def cargar_registros():
    registros = []
    if not os.path.exists(ARCHIVO):
        return registros
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            valores = linea.split(SEPARADOR)
            registros.append(dict(zip(CAMPOS, valores)))
    return registros