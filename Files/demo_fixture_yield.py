import pytest

@pytest.yield_fixture()
def setup_yield():
    print("Run before every test method")
    yield
    print("Run after every method")

def test_method_001(setup_yield):
    print("this is test method 001")

def test_method_002(setup_yield):
    print("this is test method 002")
