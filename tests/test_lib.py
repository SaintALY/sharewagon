# tests/test_lib.py
from mlproject.lib import try_me

def test_wisdome_delivery():
    assert len(try_me()) != 0
    