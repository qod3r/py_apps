import pytest
import re


def fun(s):
    """возвращает True если адрес корректный,
    иначе возвращает False"""
    reg = r"^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    if re.match(reg, s) is None:
        return False
    return True


def filter_mail(emails):
    return list(sorted(filter(fun, emails)))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    print(filtered_emails)


def get_tests():
    inputs = []
    outputs = []
    for i in range(10):
        with open(f"8_tests/input/input0{i}.txt", "r") as inp:
            r = inp.readlines()[1:]
            r = list(map(lambda s: s.rstrip("\n"), r))
            inputs.append(r)
        with open(f"8_tests/output/output0{i}.txt", "r") as out:
            outputs.append(eval(out.read()))
    return list(zip(inputs, outputs))


@pytest.mark.parametrize("input, expected", get_tests())
def test_eval(input, expected):
    assert filter_mail(input) == expected


if __name__ == "__main__":
    # main()
    print(get_tests())
