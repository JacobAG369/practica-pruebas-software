import pytest

from calculadora import sumar, restar, multiplicar, dividir

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

def test_restar_positivos():
    assert restar(8, 3) == 5

def test_restar_resultado_negativo():
    assert restar(3, 8) == -5

def test_multiplicar_valores_negativos():
    assert multiplicar(-4, -3) == 12

def test_multiplicar_un_valor_negativo():
    assert multiplicar(-4, 3) == -12

def test_dividir_exactamente():
    assert dividir(10, 2) == 5

def test_dividir_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_cero_entre_numero_no_cero():
    assert dividir(0, 5) == 0

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

@pytest.mark.parametrize(("a", "b"), [("10", 2), (10, "2"), (True, 2), (10, False)])
def test_dividir_rechaza_entradas_no_numericas(a, b):
    with pytest.raises(TypeError, match="Los valores deben ser numéricos"):
        dividir(a, b)