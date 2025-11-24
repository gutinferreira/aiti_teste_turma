import pytest
from classifica_idade import classifica_idade

@pytest.mark.parametrize("idade,categoria_esperada",[
    (5,"Criança"),
    (15,"Adolescente"),
    (30,"Adulto"),
    (60,"Idoso")

])

def test_classifica_idade(idade,categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada