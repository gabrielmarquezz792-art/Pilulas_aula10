def calcular_frete(peso_kg: float):
    if peso_kg <= 0:
        return 'R$ 0,00'
    elif peso_kg <= 1:
        return 'R$ 5,00'
    elif peso_kg <= 5:
        return 'R$ 10,00'
    return 'R$ 18,00'
