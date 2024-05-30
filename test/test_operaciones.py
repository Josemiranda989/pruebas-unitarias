import allure
from src.operaciones import sumar, restar

@allure.description("Test para sumar dos números")
@allure.feature("Operaciones")
@allure.epic("Suma")
def test_sumar():
    resultado = sumar(2, 2)
    assert resultado == 4

def test_restar():
    resultado = restar(2, 2)
    assert resultado == 0
