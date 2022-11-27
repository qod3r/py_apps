import pytest
from reverse import reverse


def test_reverse_empty():
    assert reverse("") == ""


def test_reverse_single():
    assert reverse("a") == "a"


def test_reverse_palindrome():
    assert reverse("aboba") == "aboba"


def test_reverse_string():
    assert reverse("abc") == "cba"


def test_reverse_noniter_nonstr():
    with pytest.raises(TypeError):
        reverse(11)


def test_reverse_iter_nonstr():
    with pytest.raises(TypeError):
        reverse(["a", "b", "c"])
