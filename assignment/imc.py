def calcular_imc(peso, altura): 
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
    peso (float): Peso de la persona en kilogramos.
    altura (float): Altura de la persona en metros.

    Returns:
    float: El IMC calculado.

    Raises:
    ValueError: Si el peso o la altura son menores o iguales a cero.
    """

    # Verificar si la altura es válida
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")

    # Verificar si el peso es válido
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero.")

    # Calcular y devolver el IMC
    return peso / (altura ** 2)
