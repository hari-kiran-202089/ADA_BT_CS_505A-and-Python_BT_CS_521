from Python.unique_palindromes import get_unique_palindromes


def test_get_unique_palindromes():
    assert get_unique_palindromes("abcbada") == ['ada', 'abcba']
    assert get_unique_palindromes("abcbadda") == ['adda', 'abcba']


def test_empty_string():
    assert get_unique_palindromes("") == []


def test_non_palindrome_string():
    assert get_unique_palindromes("abcdef") == []
