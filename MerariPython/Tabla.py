numero=input("Dame un número del 1 al 9: ")
numero=int(numero)

# for ejecuta un bloque de código determinado de veces
# El segundo parámetro de range no se incluye en la serie de valores
# Aquí solo sería del 1 al 10

for i in range(1,11):

    # i va derivando

    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))

