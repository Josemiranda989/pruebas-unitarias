import allure
from src.calcular_numeros import calcular_promedio

@allure.description("Test para calcular promedio de una lista de números")
@allure.feature("Números")
@allure.epic("Cálculo de promedio")
def test_calcular_promedio():
    numeros = [1, 2, 3, 4, 5]
    resultado = calcular_promedio(numeros)
    assert resultado == 3
