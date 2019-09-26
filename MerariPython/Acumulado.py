# Se declaran las variables
acumulado=int(0)
numero=str("")

# Al colocar true como condición en while, se forma un ciclo

while True:
    numero=input("Dame un número entero: ")
    if numero=="":
      # Si el número es vacío, muestra la situación y sale
      print("Vacío. Salida del programa.")
      break
    else:
      # Si se proporcionó un valor, acumulado = acumulado + numero
      # Se realiza el cálculo usando suma incluyente (+=)
      acumulado+=int(numero)
      salida="Monto acumulado: {}"
      print(salida.format(acumulado))
