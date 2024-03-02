import math

def calcular_area_superficie_lateral(radio, altura):
    return 2 * math.pi * radio * altura

def calcular_area_total(radio, altura):
    return 2 * math.pi * radio * (radio + altura)

def calcular_volumen(radio, altura):
    return math.pi * radio**2 * altura

try:
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    
    if radio <= 0 or altura <= 0:
        print("Tanto el radio como la altura deben ser números positivos.")
    else:
        area_superficie_lateral = calcular_area_superficie_lateral(radio, altura)
        area_total = calcular_area_total(radio, altura)
        volumen = calcular_volumen(radio, altura)
        
        print("El área de la superficie lateral del cilindro es:", area_superficie_lateral)
        print("El área total del cilindro (incluyendo las bases) es:", area_total)
        print("El volumen del cilindro es:", volumen)

except ValueError:
    print("Por favor, ingrese números válidos para el radio y la altura del cilindro.")
