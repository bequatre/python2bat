conjunto1 = {1, 2, 3, 4}
conjunto2 = {2, 4, 6}

conjunto1.add(5)
print(conjunto1)

#Unión (se unen todos los elementos)
union = conjunto1|conjunto2
print(union)

#Intersección (se cogen SÓLO los valores que estén en ambos conjuntos)
interseccion = conjunto1&conjunto2
print(interseccion)

#Diferencia (resta los valores que estén en ambos conjuntos)
diferencia = conjunto1-conjunto2
print(diferencia)