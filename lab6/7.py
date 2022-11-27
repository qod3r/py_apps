from numpy.polynomial import Polynomial
import numpy as np


def roots(a, b, c):
    try:
        p = Polynomial([c, b, a])
    except ValueError:
        return None
    r = p.roots()
    if r.dtype == np.complex128:
        return None
    print(r)
    return tuple(r.astype(np.float32))


def test_wrong_type():
    assert roots(1, 1, "a") is None


def test_no_roots():
    assert roots(1, 1, 1) is None


def test_same_roots():
    assert roots(1, 2, 1) == (-1, -1)


def test_diff_roots():
    assert roots(4, -6, 0) == (0, 1.5)
