from toolbox.convert_utils import tag_reading


def test_tag_reading_hot():
    assert tag_reading(30) == ["chaud"]


def test_tag_reading_cold_is_independent():
    tag_reading(30)  # premier appel, sans rapport avec le second
    assert tag_reading(10) == ["froid"]  # échoue actuellement, voir issues/002
