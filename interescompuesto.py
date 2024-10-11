#p = capital inicial
p = 0

#t = numero de años
t = 0

#r = interes
r = 0

#n = intervalo de cobro
n = 12

#calcular el interés
def calcularInteres(p, t, r, n):
    capital_final = p*(1+r/n)**(n*t)
    return capital_final

#damos los datos
p = float(input("Dime cuál es el capital inicial (€): "))
#t = float(input("Dime cuál es el número de años: "))
r = float(input("Dime cuál es el interés (%): "))/100

#calculamos el interés
capital_final = calcularInteres(p, t, r, n)

#imprimimos en pantalla el valor del capital final
print(p)
print(t)
print(r)
print(n)
#print(f"La cantidad final despues de {int(t)} años será de: {capital_final}€.")

t = 1
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 1 años será de: {capital_final}€.")
t = 2
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 2 años será de: {capital_final}€.")
t = 3
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 3 años será de: {capital_final}€.")
t = 4
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 4 años será de: {capital_final}€.")
t = 5
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 5 años será de: {capital_final}€.")
t = 6
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 6 años será de: {capital_final}€.")
t = 7
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 7 años será de: {capital_final}€.")
t = 8
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 8 años será de: {capital_final}€.")
t = 9
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 9 años será de: {capital_final}€.")
t = 10
capital_final = calcularInteres(p, t, r, n)
print(f"La cantidad final despues de 10 años será de: {capital_final}€.")