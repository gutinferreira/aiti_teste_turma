import pytest
from soma import soma

@pytest.mark.parametrize('a,b,esperado',[(1,2,3)])
def test_soma(a,b,esperado):
    assert soma(a,b) == esperado