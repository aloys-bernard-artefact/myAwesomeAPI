import pytest
from src.world import hello


def test_dummy():
    """Dummy test to test the test framework."""
    assert True


@pytest.mark.parametrize("name", ["Bob", "Alice", "Charlie"])
def test_hello(name):
    assert hello(name) == "Hello, {}!".format(name)


def test_mock(mocker):
    mock = mocker.MagicMock()
    mock.return_value = 3
    assert mock() == 3
