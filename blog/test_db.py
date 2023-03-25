from .db import get_engine

def test_get_engine():
    try:
        engine = get_engine()
    except Exception as exc:
        assert False, f'test_get-engine raised an exception {exc}'