import pytest
from calcula_total import calcula_total

@pytest.mark.parametrize("preco",[10.00,50.00,100.00])
@pytest.mark.parametrize("perc_desconto",[0.00,0.10,0.25])
@pytest.mark.parametrize("perc_imposto",[0.00,0.05,0.10])

def test_calcula_total(preco, perc_desconto, perc_imposto):
    desconto_esperado = preco * perc_desconto
    imposto_esperado = (preco - desconto_esperado) * perc_imposto
    total_esperado = preco - desconto_esperado + imposto_esperado
    assert calcula_total(preco,perc_desconto,perc_imposto) == round(total_esperado,2)

