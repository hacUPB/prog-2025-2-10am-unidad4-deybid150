# Simulaciones de lanzamiento de cohete

def sim_cohete(etapas):
    objetivo_alt = 200
    altitud = 0
    minuto = 0
    etapa_actual = 0

    while altitud < objetivo_alt and etapa_actual < len(etapas):
        etapa = etapas[etapa_actual]

        if etapa["combustible"] > 0:
            etapa["combustible"] -= etapa["consumo"]
            altitud += etapa["ascenso"]
            minuto += 1
        else:
            etapa_actual += 1  # pasa a la siguiente etapa

    if altitud >= objetivo_alt:
        print(" El cohete alcanzó la órbita de 200 km en", minuto, "minutos.")
    else:
        print("El cohete se quedó sin combustible en la etapa {etapa_actual + 1}.")
        print("Altitud alcanzada:", altitud, "km")

# Bucle principal
while True:
    print("Simulación de lanzamiento de cohete")

    # Lista de diccionarios: una por cada etapa
    etapas = [
        {
            "nombre": "Etapa 1",
            "consumo": 800,
            "ascenso": 5,
            "combustible": int(input("Ingrese la cantidad de combustible de la etapa 1 (kg): "))
        },
        {
            "nombre": "Etapa 2",
            "consumo": 500,
            "ascenso": 3,
            "combustible": int(input("Ingrese la cantidad de combustible de la etapa 2 (kg): "))
        }
    ]

    sim_cohete(etapas)

    continuar = input("\n¿Desea realizar otra simulación? (SI/NO): ").upper()
    if continuar == "NO":
        print("Simulación finalizada.")
        break



