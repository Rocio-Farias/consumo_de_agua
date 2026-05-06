
def calcular_objetivo_ml(peso_kg, nivel_actividad):
    objetivo_base = peso_kg * 35 

    if nivel_actividad == "bajo":
        objetivo = objetivo_base * 0.9
    elif nivel_actividad == "medio":
        objetivo = objetivo_base
    elif nivel_actividad == "alto":
        objetivo = objetivo_base * 1.1
    else:
        objetivo = objetivo_base  # por seguridad

    return objetivo



def estado_hidratacion(consumo_ml, objetivo_ml):
    if consumo_ml < objetivo_ml:
        diferencia = objetivo_ml - consumo_ml
        porcentaje = (diferencia / objetivo_ml) * 100
        return f"Te falta un {porcentaje:.2f}% para llegar"
    elif consumo_ml == objetivo_ml:
        return "Has alcanzado tu objetivo"
    else:
        exceso = consumo_ml - objetivo_ml
        porcentaje = (exceso / objetivo_ml) * 100
        return f"Has excedido tu objetivo en {porcentaje:.2f}%"



personas = []

while True:
    try:
        print("\n--- Nueva persona ---")

        peso = float(input("Ingrese el peso: "))

        while True:
            actividad = input("Ingrese nivel de actividad (bajo / medio / alto): ")
            if actividad in ["bajo", "medio", "alto"]:
                break
            else:
                print("Nivel de actividad inválido. Intente de nuevo.")

        consumo = float(input("Ingrese cantidad de agua consumida (ml): "))

        objetivo = calcular_objetivo_ml(peso, actividad)
        estado = estado_hidratacion(consumo, objetivo)

        print(f"Objetivo diario: {objetivo:.2f} ml")
        print(f"Estado: {estado}")

       
        persona = {
            "peso": peso,
            "actividad": actividad,
            "consumo": consumo,
            "objetivo": objetivo
        }

        personas.append(persona)

     
        seguir = input("¿Desea cargar otra persona? (si/no): ")
        if seguir != "si":
            break

    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")



print("\n=== RESUMEN DE PERSONAS ===")
for i, p in enumerate(personas, start=1):
    print(f"\nPersona {i}:")
    print(f"Peso: {p['peso']}")
    print(f"Actividad: {p['actividad']}")
    print(f"Consumo: {p['consumo']} ml")
    print(f"Objetivo: {p['objetivo']:.2f} ml")
     