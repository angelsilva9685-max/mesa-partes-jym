import os # Herramienta del sistema operativo para verificar si el archivo existe en el disco duro

# variables fijas ya configuradas para el programa. No se deben cambiar.
ARCHIVO = "guias.txt"
SEPARADOR = "|"
CAMPOS = ["codigo_sunat", "ruc_cliente", "ruc_proveedor", "fecha",
          "punto_salida", "punto_llegada", "peso", "items",
          "cantidades", "receptor", "orden_compra", "comprobante"]

# Abre el archivo en modo "a" (agregar) para escribir al final sin borrar lo anterior
def guardar_registro(datos):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        linea = SEPARADOR.join(str(datos[campo]) for campo in CAMPOS)
        f.write(linea + "\n")

# Crea la caja vacía donde guardaremos la informacion del archivo.txt y la devuelve como una lista de diccionarios
# a las funciones que la llamen como registrar, buscar y ordenar.
def cargar_registros():
    registros = []
    if not os.path.exists(ARCHIVO): # Si el archivo "guias.txt" NO existe físicamente en la computadora
        return registros # devuelve la lista vacia para que el programa no se rompa y pueda seguir funcionando
    with open(ARCHIVO, "r", encoding="utf-8") as f: # Si el archivo sí existe, lo abre en modo "r" (leer)
        for linea in f: #limpia los Enters invisibles (\n) y espacios de los costados
            linea = linea.strip()
            if not linea: #if linea está vacía, salta a la siguiente vuelta del bucle y no hace nada
                continue
            valores = linea.split(SEPARADOR) # El cierre (zip): Empareja las etiquetas (CAMPOS) con los datos (valores), 
            # lo convierte en un Diccionario, y lo guarda (.append) dentro de la caja
            registros.append(dict(zip(CAMPOS, valores)))        
    return registros # Termina de leer todo y entrega la caja llena con todos los diccionarios