def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    resultado = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            clave = columnas[0]

            # Columna 5: lista de pares tipo "abc:12"
            pares = columnas[4].split(",")
            suma = 0

            for par in pares:
                # Obtener el número después de ":"
                _, num = par.split(":")
                suma += int(num)

            # Acumular por clave
            if clave in resultado:
                resultado[clave] += suma
            else:
                resultado[clave] = suma

    return resultado
