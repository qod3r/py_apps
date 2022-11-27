import pytest
from pprint import pprint
import numpy as np

np.set_printoptions(suppress=True)


def is_under_queen_attack(pos, qpos):
    letters = "abcdefgh"
    if not isinstance(pos, str) or not isinstance(qpos, str):
        raise TypeError("not a str")
    if len(pos) != 2 or len(qpos) != 2:
        raise ValueError("position is too long")
    if pos[0] not in letters or qpos[0] not in letters:
        raise ValueError("incorrect position")
    if int(pos[1]) > 8 or int(qpos[1]) > 8:
        raise ValueError("incorrect position")

    pos = (letters.index(pos[0]), int(pos[1]) - 1)
    qpos = (letters.index(qpos[0]), int(qpos[1]) - 1)
    board = np.zeros([8, 8], dtype=np.int8)

    # same x
    # same y
    board[7 - qpos[1], :] = 1
    board[:, qpos[0]] = 1
    for i in range(8):
        for j in range(8):
            # secondary diag
            if 7 - i - j == 7 - qpos[0] - qpos[1]:
                board[7 - i][j] = 1
            # main diag
            if i - 7 - j == qpos[0] - 7 - qpos[1]:
                board[i][7 - j] = 1
    board[7 - qpos[1], qpos[0]] = 2
    print(board)
    if board[7 - pos[1], pos[0]] > 0:
        return True
    return False


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, 42)


def test_wrong_coordinate():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "42")


def test_wrong_coordinate2():
    with pytest.raises(ValueError):
        is_under_queen_attack("c3", "d4d")


def test_wrong_coordinate_out_of_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack("e1", "e9")


def test_attack_same_field():
    assert is_under_queen_attack("e5", "e5")


def test_attack_same_row():
    assert is_under_queen_attack("a1", "e1")


def test_attack_same_column():
    assert is_under_queen_attack("a1", "a8")


def test_attack_diagonal():
    assert is_under_queen_attack("b3", "e6")


def test_no_attack():
    assert not is_under_queen_attack("c4", "e5")


is_under_queen_attack("a1", "c4")
