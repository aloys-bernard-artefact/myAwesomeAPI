from src.cat import Cat
import pytest


@pytest.fixture()
def _cat():
    return Cat("Kitty")
