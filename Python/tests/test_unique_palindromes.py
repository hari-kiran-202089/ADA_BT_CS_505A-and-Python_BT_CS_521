from webbrowser import get
from Python.unique_palindromes import get_unique_palindromes


def test_get_unique_palindromes():
    assert get_unique_palindromes("abcbada") == ['abcba', 'ada']
    assert get_unique_palindromes("abcbadda") == ['abcba', 'adda']


def test_empty_string():
    assert get_unique_palindromes("") == []


def test_non_palindrome_string():
    assert get_unique_palindromes("abcdef") == []
