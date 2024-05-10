## the purpose of  test fixture is to provide a fixed baseline upon which test  can reliably and
# repeatedly execute
## @pytest.fixture() = execute the specific method defore every test method
## @pytest.yield_fixture() = execute the specific method defore and after every test method

import pytest


@pytest.fixture()
def setup():
    print("Run before every test method")


def test_method_001(setup):
    print("this is test method 001")


def test_method_002(setup):
    print("this is test method 002")


