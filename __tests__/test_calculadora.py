import pytest

#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculadora')))

from utils.utils import *
from calculadora.calculadora import *


def test_soma_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Act - Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_atual == resultado_esperado


def test_subtrair_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 10
    num2 = 8
    resultado_esperado = 2

    # Act - Executa
    resultado_atual = subtrair_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_atual == resultado_esperado


def test_multiplicar_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 4
    resultado_esperado = 20

    # Act - Executa
    resultado_atual = multiplicar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_atual == resultado_esperado


def test_dividir_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 10
    num2 = 2
    resultado_esperado = 5

    # Act - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_atual == resultado_esperado


def test_dividir_por_zero():
    # AAA

    # Arrange - Configura
    num1 = 10
    num2 = 0
    resultado_esperado = "Não é possível dividir por zero."

    # Act - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_atual == resultado_esperado


@pytest.mark.parametrize('num1, num2, resultado_esperado', [
    (5,7,12), # Parametrização dos testes
    (3,0,3),
    (-1,6,5),
    (-9,-2,-11),
    (0.5, 0.25, 0.75)
])
def test_soma_dois_numeros_lista(num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vem da lista acima (parametrize)
    #num1 = 5
    #num2 = 7
    #resultado_esperado = 12

    # Act - Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_atual == resultado_esperado


@pytest.mark.parametrize('num1, num2, resultado_esperado',
    ler_csv('./fixtures/csv/massa_somar.csv')
)
def test_soma_dois_numeros_lista(num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vem da lista acima (parametrize)
    #num1 = 5
    #num2 = 7
    #resultado_esperado = 12

    # Act - Executa
    resultado_atual = somar_dois_numeros(float(num1), float(num2))

    # Assert - Valida
    assert resultado_atual == float(resultado_esperado)


@pytest.mark.parametrize('largura, comprimento, resultado_esperado', [
    (2,5,5), # Parametrização dos testes
    (10,5,25),
    (5.5,7.35,20.2125),
    (20,50,500),
    (15.5,20.9,161.975),
])
def test_area_do_triangulo(largura, comprimento, resultado_esperado):


    # Arrange - Configura
    # Dados vem da lista acima (parametrize)


    # Act - Executa
    resultado_atual = area_do_triangulo(float(largura), float(comprimento))

    # Assert - Valida
    assert resultado_atual == float(resultado_esperado)


@pytest.mark.parametrize('largura, comprimento', [
    (2,-5), # Parametrização dos testes
    (-10,5),
    (5.5,-7.35),
    (-20,-50),
    (-15.5,20.9),
])
def test_area_do_triangulo_valor_negativo(largura, comprimento):


    # Arrange - Configura
    # Dados vem da lista acima (parametrize)

    resultado_esperado = 'Largura e comprimento não podem ser negativos.'

    # Act - Executa
    resultado_atual = area_do_triangulo_negativo(float(largura), float(comprimento))

    # Assert - Valida
    assert resultado_atual == resultado_esperado