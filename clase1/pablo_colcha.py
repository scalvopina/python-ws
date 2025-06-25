#ejercicio 1

def person():
    name = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))  
    peso = float(input("Ingrese su peso: "))    
    talla = float(input("Ingrese su talla: "))
    return name, edad, talla, peso
    
def calcular_imc(peso, talla):
    peso = float(input("Ingrese su peso: "))
    talla = float(input("Ingrese su talla: "))
    return peso / talla ** 2

def clasificar_imc(imc):
    imc = peso / talla ** 2
    if (imc < 18.5):
        mensaje="Bajo peso"
    elif imc < 25:
        mensaje="Peso normal"
    elif imc < 30:
        mensaje="Sobrepeso"
    else:
        mensaje="Obesidad"
    return mensaje

def ejercicio1(peso, talla):
    imc = calcular_imc(peso, talla)
    mensaje = clasificar_imc(imc)
    return mensaje

if __name__ == "__main__":
    name, edad, talla, peso = person()
    msm =ejercicio1(peso, talla)
    print(f"Hola {name},tienes {edad} años y estas en: {msm}")
    
    
    
#ejercicio 2
    