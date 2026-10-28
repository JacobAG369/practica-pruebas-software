def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Los valores deben ser numéricos")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Los valores deben ser numéricos")
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b