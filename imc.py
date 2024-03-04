def calcular_imc(peso, altura):
    # convertir altura centímetros a metros
    altura_m = altura / 100
    
    # calculo IMC
    imc = peso / (altura_m ** 2)
    
    # redondear el IMC en 2 decimales
    imc = round(imc, 2)
    
    # clasificación del IMC según la OMS
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc <= 25:
        clasificacion = "Adecuado"
    elif 25 < imc <= 30:
        clasificacion = "Sobrepeso"
    elif 30 < imc <= 35:
        clasificacion = "Obesidad grado I"
    elif 35 < imc <= 40:
        clasificacion = "Obesidad grado II"
    else:
        clasificacion = "Obesidad grado III"
    
    return imc, clasificacion

if __name__ == "__main__":
    # ingrese el peso y la altura
    peso = float(input("Ingrese peso en kg: "))
    altura = float(input("Ingrese altura en centímetros: "))
    
    # calcular el IMC y la clasificación
    imc, clasificacion = calcular_imc(peso, altura)
    
    # mostrar el resultado
    print(f"Su IMC es {imc}")
    print(f"La clasificación OMS es {clasificacion}")
