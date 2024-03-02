import math

def calcular_longitud_y_area(radio):
    longitud = 2 * math.pi * radio
    area_circuito_inscrito = math.pi * radio ** 2
    return longitud, area_circuito_inscrito

def main():
    radio = float(input("Ingrese el radio de la circunferencia: "))
    longitud, area_circuito_inscrito = calcular_longitud_y_area(radio)
    print(f"Longitud de la circunferencia: {longitud}")
    print(f"Área del círculo inscrito: {area_circuito_inscrito}")

if __name__ == "__main__":
    main()
