numero1=input("Número 1: ")
numero2=input("Número 2: ")
salida="Números proporcionados: {} y {}. {}."
if (numero1==numero2):

    # Entra aquí si los números tecleados son iguales.

    print(salida.format(numero1, numero2, "Los números son iguales"))
else:

    # Condicionales integradas, if dentro de otro if
    # Si los números son iguales

    if numero1>numero2:

        # Muestra si el primero número es mayor al segundo
        print(salida.format(numero1, numero2, "El mayor es el primero"))

    else:
        # O al contrario, si el primero no es mayor al segundo
        print(salida.format(numero1, numero2, "El mayor es el segundo"))


