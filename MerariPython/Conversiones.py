# Se declara la variable str con 4 dígitos
numero= "1234"
# Se muestra el tipo de variable
# el type no es un str, es un dato type
print(type(numero))
# La cadena se convierte a su equivalente int
numero=int(numero)
# Se muestra como cambió el tipo pero se usa la misma variable
print(type(numero))
# Se declara la str con sustitución
salida="El número utilizado es {}"
# Al final se muestra el resultado
# La sustitución hará que en los corchetes se coloque el valor del número
print(salida.format(numero))
