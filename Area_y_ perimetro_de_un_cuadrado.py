def calcular_area(lado):
    return lado * lado

def calcular_perimetro(lado):
    return 4 * lado

try:
    lado = float(input("Ingrese la longitud del lado del cuadrado: "))
    
    if lado <= 0:
        print("La longitud del lado debe ser un número positivo.")
    else:
        area = calcular_area(lado)
        perimetro = calcular_perimetro(lado)
        
        print("El área del cuadrado es:", area)
        print("El perímetro del cuadrado es:", perimetro)

except ValueError:
    print("Por favor, ingrese un número válido para la longitud del lado del cuadrado.")
