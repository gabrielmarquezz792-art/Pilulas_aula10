def converter_nota_para_conceito(nota: float):
    if nota > 10 or nota < 0:
        return 'Nota inválida'
    elif nota < 3:
        return 'Conceito F'
    elif nota <= 4.9:
        return 'Conceito D'
    elif nota <= 6.9:
        return 'Conceito C'
    elif nota <= 8.9:
        return 'Conceito B'  
    return 'Conceito A'
