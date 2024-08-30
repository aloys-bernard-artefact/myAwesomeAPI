from src.cat import Cat
import pytest


@pytest.fixture()
def cat():
    return Cat("Kitty")
