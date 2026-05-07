from exercicio3 import converter_nota_para_conceito

def test_nota_9_10():
    assert converter_nota_para_conceito(10.0) == 'Conceito A'
    assert converter_nota_para_conceito(9.0) == 'Conceito A'

def test_nota_7_8():
    assert converter_nota_para_conceito(8.9) == 'Conceito B'
    assert converter_nota_para_conceito(7.0) == 'Conceito B'

def test_nota_5_6():
    assert converter_nota_para_conceito(6.9) == 'Conceito C'
    assert converter_nota_para_conceito(5.0) == 'Conceito C'

def test_nota_3_4():
    assert converter_nota_para_conceito(4.9) == 'Conceito D'
    assert converter_nota_para_conceito(3.0) == 'Conceito D'

def test_nota_3():
    assert converter_nota_para_conceito(2.9) == 'Conceito F'
    assert converter_nota_para_conceito(0.0) == 'Conceito F'

def test_nota_invalida():
    assert converter_nota_para_conceito(-1.0) == 'Nota inválida'
    assert converter_nota_para_conceito(10.1) == 'Nota inválida'
