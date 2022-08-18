from ADA.binary_search import binary_search
import pytest


@pytest.fixture
def get_array():
    return [1, 3, 5, 7, 9, 12, 34, 45, 77, 87, 99, 143]


def test_binary_search(get_array):
    assert binary_search(get_array, 1) == 0
    assert binary_search(get_array, 143) == 11


def test_mid_values(get_array):
    assert binary_search(get_array, 34) == 6
    assert binary_search(get_array, 45) == 7


def test_not_existing_values(get_array):
    assert binary_search(get_array, 43) == -1
    assert binary_search(get_array, 0) == -1
