entrada=input()
print(type(entrada))

# La variable booleana tiene el resultado a verificar
# si lo tecleado es un digito y si no hay punto
# se trata de un número con decimales, o sea float
# Si la busqueda devuelve -1 quiere decir que no se encontro punto
# Si es entero es true, lo tecleado es entero.

esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    # Si la condición es verdadera (true)

    print("Dato entero. ¡Muy bien!")
else:
  # Si la condición es falsa (false)

  print("Dato no es entero. Intentar nuevamente.")
