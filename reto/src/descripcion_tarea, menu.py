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
        print(f"El cohete se quedó sin combustible en la etapa {etapa_actual + 1}.")
        print("Altitud alcanzada:", altitud, "km")

def menu():
    print("\n--- MENU ---")
    print("R: Simular cohete")
    print("D: Diccionario")
    print("S: Salir")
    return input("Seleccione una opción: ").strip().upper()

 # Lista de diccionarios: una por cada etapa
def etapas(): 
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
    return etapas

def diccionario():
    print("\n mostrar informacion del diccionario.")
    for i, etapa in enumerate(etapas, start=1):
        print(f"\n etapa {i}:")
        for keys, values in etapa.items():
            print(f"{keys}:{values}")

# Bucle principal
e = True
while e == True:
    O = menu()
    match O:
        case "R":
            print("Simulación de lanzamiento de cohete")
            sim_cohete(etapas())

            continuar = input("\n¿Desea realizar otra simulación? (SI/NO): ").upper()
            if continuar == "NO":
                print("Simulación finalizada.")
                break
        case "D":
         diccionario()
        case "S":
            print("saliendo del programa...")
            e = False
        case _:
            print("dele bien, entrada no valida")
