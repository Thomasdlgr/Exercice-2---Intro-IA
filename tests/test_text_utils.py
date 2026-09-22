from toolbox.text_utils import is_palindrome, word_frequency


def test_is_palindrome_simple():
    assert is_palindrome("radar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("un roc si biscornu") is True  # échoue actuellement, voir issues/001


def test_is_palindrome_false():
    assert is_palindrome("python") is False


# --- word_frequency ---


def test_word_frequency_basic():
    result = word_frequency("le chat et le chien")
    assert result == {"le": 2, "chat": 1, "et": 1, "chien": 1}


def test_word_frequency_case_insensitive():
    result = word_frequency("Hello hello HELLO")
    assert result == {"hello": 3}


def test_word_frequency_ignores_punctuation():
    result = word_frequency("Hello, world! Hello...")
    assert result == {"hello": 2, "world": 1}


def test_word_frequency_empty():
    assert word_frequency("") == {}


def test_word_frequency_numbers_ignored():
    result = word_frequency("abc 123 def 123 ghi")
    assert result == {"abc": 1, "def": 1, "ghi": 1}


def test_word_frequency_single_word():
    assert word_frequency("python") == {"python": 1}
