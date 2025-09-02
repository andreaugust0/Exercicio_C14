import numpy as np
from exercicio_c14.main import criar_array, calcular_estatisticas

class TestCriarArray:
    def test_array_criado_corretamente(self):
        numeros = [1, 2, 3]
        resultado = criar_array(numeros)
        esperado = np.array([1, 2, 3])
        assert np.array_equal(resultado, esperado)

    def test_array_errado(self):
        numeros = [1, 2, 3]
        resultado = criar_array(numeros)
        esperado = np.array([1, 2, 4])
        assert np.array_equal(resultado, esperado)


class TestCalcularEstatisticas:
    def test_estatisticas_corretas(self):
        array = np.array([1, 2, 3, 4])
        resultado = calcular_estatisticas(array)
        esperado = {"soma": 10, "media": 2.5, "maximo": 4}
        assert resultado == esperado

    def test_estatisticas_erradas(self):
        array = np.array([1, 2, 3, 4])
        resultado = calcular_estatisticas(array)
        esperado = {"soma": 11, "media": 3.0, "maximo": 5}
        assert resultado == esperado

    def test_estatisticas_array_negativos(self):
        array = np.array([-5, -2, -3])
        resultado = calcular_estatisticas(array)
        esperado = {"soma": -10, "media": -10/3, "maximo": -2}
        assert resultado == esperado

    def test_estatisticas_array_negativos_errado(self):
        array = np.array([-5, -2, -3])
        resultado = calcular_estatisticas(array)
        esperado = {"soma": -9, "media": -3.0, "maximo": -3}
        assert resultado == esperado
