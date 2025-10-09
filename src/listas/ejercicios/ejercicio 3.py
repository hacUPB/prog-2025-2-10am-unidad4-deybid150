tiempo = [0, 10, 20, 30, 40, 50, 60]
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]
velocidad = [0, 50, 100, 150, 200, 250, 300]
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelacion"]

print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado):
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")