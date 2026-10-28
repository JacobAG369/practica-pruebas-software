import pytest

from calculadora import sumar, dividir

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

def test_dividir_exactamente():
    assert dividir(10, 2) == 5

def test_dividir_decimal():

    assert dividir(7, 2) == 3.5

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

@pytest.mark.parametrize(("a", "b"), [("10", 2), (10, "2"), (True, 2), (10, False)])
def test_dividir_valores_no_numericos(a, b):
    with pytest.raises(TypeError, match="Los valores deben ser numéricos"):
        dividir(a, b)