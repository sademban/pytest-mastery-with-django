import pytest

@pytest.mark.slow
def test_example():
    print("test1")
    assert 1 == 1

def test_example1():
    assert 1 == 1