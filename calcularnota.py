bachiller = 0
general = 0
optativa1 = 0
optativa2 = 0
p1 = 0
p2 = 0
nota_medicina = 12.61

def calcularNota(bachiller, general, optativa1, optativa2, p1, p2):
    nota_final = bachiller*0.6 + general*0.4 + optativa1*p1 + optativa2*p2
    return nota_final

bachiller = float(input("Dime cuál es tu nota media de bachiller: "))
general = float(input("Dime cuál es tu nota media de la fase general de selectividad: "))
optativa1 = float(input("Dime cuál es tu nota de la primera optativa de selectividad: "))
optativa2 = float(input("Dime cuál es tu nota de la segunda optativa de selectividad: "))
p1 = float(input("Dime cuánto pondera la primera optativa (en decimales): "))
p2 = float(input("Dime cuánto pondera la segunda optativa (en decimales): "))

nota_final = float(calcularNota(bachiller, general, optativa1, optativa2, p1, p2))

print(f"Tu nota final para el acceso a la universidad es: {round(nota_final, 2)}.")

if(nota_final < nota_medicina):
    print("La nota no es suficiente para entrar en la carrera de medicina en la UIB.")
else:
    print("La nota es suficiente para entrar en la carrera de medicina en la UIB, ¡felicidades!")