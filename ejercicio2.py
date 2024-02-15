from math import pow
def calcular_capital_final(capital_inicial, tasa_interes, num_anios):
    tasa_interes_decimal = tasa_interes / 100
    capital_final = capital_inicial * (1 + tasa_interes_decimal) ** num_anios
    return capital_final

def calcular_capital_final(capital_inicial, tasa_interes, num_anios):
    tasa_interes_decimal = tasa_interes / 100
    capital_final = capital_inicial * pow((1 + tasa_interes_decimal), num_anios)
    return capital_final

def main():
    capital_inicial = float(input("Ingrese el capital inicial: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual (entre 1% y 10%): "))
    while tasa_interes < 1 or tasa_interes > 10:
        tasa_interes = float(input("La tasa de interés debe estar entre 1% y 10%. Ingrese nuevamente: "))

    num_anios = int(input("Ingrese el número de años: "))

    capital_final = calcular_capital_final(capital_inicial, tasa_interes, num_anios)

    print("El capital final es:", capital_final)

if __name__ == "__main__":
    main()
