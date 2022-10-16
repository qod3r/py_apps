def has_digits(s):
    return any(char.isdigit() for char in s)

def has_lowercase(s):
    return any(char.isupper() for char in s)

def has_uppercase(s):
    return any(char.islower() for char in s)

def has_length(s):
    return len(s) > 8

def not_lazy(s):
    layouts = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"]
    # 0123456789
    # qawsasdwew
    for l in layouts:
        for i in range(len(l) - 2):
            # print(l[i:i+3])
            if l[i:i+3] in s:
                return False
    return True

while True:
    pw = input("> ")
    try:
        assert has_digits(pw)
        assert has_digits(pw)
        assert has_lowercase(pw)
        assert has_uppercase(pw)
        assert has_length(pw)
        assert not_lazy(pw)
    except AssertionError:
        print("error")
    else:
        print("ok")
