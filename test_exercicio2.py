from exercicio2 import calcular_frete

def test_kilo1():
    assert calcular_frete(1.0) == 'R$ 5,00'

def test_kilo5():
    assert calcular_frete(1.01) == 'R$ 10,00'
    assert calcular_frete(5.0) == 'R$ 10,00'

def test_kilo_maior5():
    assert calcular_frete(5.01) == 'R$ 18,00'

def test_kilo_invalido():
    assert calcular_frete(0.0) == 'R$ 0,00'
    assert calcular_frete(-10.0) == 'R$ 0,00'
