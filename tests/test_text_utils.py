from toolbox.text_utils import is_palindrome


def test_is_palindrome_simple():
    assert is_palindrome("radar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("un roc si biscornu") is True  # échoue actuellement, voir issues/001


def test_is_palindrome_false():
    assert is_palindrome("python") is False
