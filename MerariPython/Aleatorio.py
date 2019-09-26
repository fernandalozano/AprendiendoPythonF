# Para utilizar un módulo en python primero tiene que importarse

import random

# Se define la variable float, también se le asigna un valor

numero1=float(10.5)

# Las funciones son conjuntos de instrucciones
# Y en python procesan una tarea especifica
# Se declaran con def

def miFuncion():

    # El número aleatorio generado por random
    # se convierte en float

    numero2=float(random.randrange(1,10))

    # Se utilizan las meta en sustituciones para mostrar resultados

    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Por último se ejecuta la función ya definida

miFuncion()



