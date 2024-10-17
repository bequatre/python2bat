#Creamos una variable que incluye varios valores
miLista = [1, 2, 3, 4]

#Si imprimimos la lista sin especificar la posición del valor, se imprimen todos los valores
print(miLista)

#Aquí elegimos la posición del valor con [] para elegirlo
print(miLista[2]) #Se imprimirá 3, ya que está en la posición dos de "miLista"

#Creamos una lista de ingredientes
ingredientes = ["huevos", "patatas"]
ingredientes.append("cebolla") #Así se añade un elemento a la lista

#Vemos como salen los tres ingredientes
print(ingredientes)

#Imprime cada uno de los ingredientes en líneas diferentes
for ingrediente in ingredientes:
    print(ingrediente)

#Ordena alfabéticamente los elementos de la lista
ingredientes.sort()
print(ingredientes)

#la función "pop" saca el último ingrediente de la lista
ingredientes.pop()
print(ingredientes)