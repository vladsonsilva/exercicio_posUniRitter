from Calculadora import Calculadora

def test_soma():
    calculadora = Calculadora()
    resultado = calculadora.soma(1,1)
    assert resultado == 2