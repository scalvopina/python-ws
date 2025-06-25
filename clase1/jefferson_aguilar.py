# EJERCICIO 1

def ejercicio1(peso, talla):
    peso = float(peso)
    talla = float(talla)
    imc = peso/(talla*talla)
    if (imc < 18.5):
        mensaje = " es Bajo"
    elif (imc < 25):
        mensaje = " es Saludable"
    elif (imc < 30):
        mensaje = "es Sobrepeso"
    else:
        mensaje = " es Obesidad"
    return mensaje


if __name__ == "__main__":

    name = input("El Nombre es: ")
    edad = input("La Edad es: ")
    peso = input("El Peso en kg. es: ")
    talla = input("La Talla m. es: ")
    msn = ejercicio1(peso, talla)
    print(f"Hola {name}, tienes {edad} años y tu peso es {msn}")

  #  ejercicio2()