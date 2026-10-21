# Importamos la función cargar_registros desde archivo.py para poder acceder a los registros guardados en el archivo de texto
from archivo import cargar_registros

# resive el codigo ingreso por el usuario y busca en la caja de registros si existe
# . Si lo encuentra, devuelve el diccionario con los datos de la guía; si no lo encuentra, devuelve None.
def buscar(codigo):
    registros = cargar_registros()
    for registro in registros:
        if registro["codigo_sunat"] == codigo:
            return registro
    return None