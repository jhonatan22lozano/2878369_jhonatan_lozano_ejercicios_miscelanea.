# Función para calcular el área del triángulo
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

# Solicitar al usuario la entrada de la base y la altura del triángulo
base = float(input("Ingrese la longitud de la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Calcular el área del triángulo
area_triangulo = calcular_area(base, altura)

# Imprimir el resultado
print("El área del triángulo con base {} y altura {} es: {}".format(base, altura, area_triangulo))
