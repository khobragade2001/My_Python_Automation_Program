import pytest


@pytest.mark.smoke
def test_a():
    print("this is test method a")

@pytest.mark.smoke
def test_b():
    print("this is test method b")

@pytest.mark.regression
def test_c():
    print("this is test method c")

@pytest.mark.skip
def test_d():
    print("this is test method d")
