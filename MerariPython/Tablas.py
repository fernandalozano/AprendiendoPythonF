for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))

    # el print sin argumentos es un salto de línea

    print()

    # Dentro de un for se pone otro for

    for j in range(1,11):

        # Aquí la i contiene el número base de la tabla
        # y j el elemento de la tabla

        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        # Al finalizar las interaciones que se indican
        # se ejecuta el código con salto de línea

        print()

