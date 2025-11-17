import utilidades.utilidades as util
import pytest

@pytest.mark.parametrize("txt, segundos",[
    ("0y:0M:0w:3d:0h:0m:0s",259200),
    ("0y:0M:2w:0d:0h:0m:0s",1209600),
])
def test_frecuencia_valida(txt,segundos):
    assert util.calcular_frecuencia(txt) == segundos