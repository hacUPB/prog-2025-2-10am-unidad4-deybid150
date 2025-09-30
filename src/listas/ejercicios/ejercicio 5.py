
import random
numeros = []
for i in range(100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)

suma = 0
for i in numeros:
    suma += i
Pr = suma/100

menor = min(numeros)
mayor = max(numeros)

print(f"la lista es {numeros}, el promedio de la lista es: {Pr} y los numeros maximos y minimos son: {mayor}, {menor} respectivamente")