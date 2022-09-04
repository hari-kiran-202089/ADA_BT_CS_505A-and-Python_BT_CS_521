from ADA.mergesort import mergesort


def test_mergesort():
    assert mergesort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_repeated_values():
    assert mergesort([1, 2, 3, 1, 2, 3]) == [1, 1, 2, 2, 3, 3]
