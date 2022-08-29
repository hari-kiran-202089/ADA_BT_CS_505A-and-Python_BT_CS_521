from Python.permutations_of_length_3 import permutaions_of_3


def test_permutations_of_3():
    assert set(permutaions_of_3("abc")) == set([
        'abc', 'acb', 'bac', 'bca', 'cab', 'cba'])


def test_emptystring():
    assert set('') == set(permutaions_of_3(""))


def test_duplicate_characters():
    assert set(['aaa']) == set(permutaions_of_3("aaa"))
    assert set(['aab', 'baa', 'aba']) == set(permutaions_of_3("aab"))
