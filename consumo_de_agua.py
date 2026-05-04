def calcular_objetivo_ml(peso_kg, nivel_actividad):
    objetivo = peso_kg * 35

    if nivel_actividad == "bajo":
        objetivo *= 0.9
    elif nivel_actividad == "alto":
        objetivo *= 1.1

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

        peso = float(input("Ingrese el peso en kg: "))

        while True:
            actividad = input("Ingrese nivel de actividad (bajo / medio / alto): ")
            if actividad in ["bajo", "medio", "alto"]:
                break
            else:
                print("Nivel de actividad inválido. Intente de nuevo.")

        consumo = float(input("Ingrese cantidad de agua consumida (ml): "))

        objetivo = calcular_objetivo_ml(peso, actividad)
        estado = estado_hidratacion(consumo, objetivo)

    
        objetivo = calcular_objetivo_ml (peso, actividad)
        estado= estado_hidratacion (consumo,  objetivo)
        
        print("Objetivo diario: {objetivo:.2f} ml")
        print("Estado:", estado)
     