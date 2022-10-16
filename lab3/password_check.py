class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class SequenceError(PasswordError):
    pass


def check_password(s):
    layouts = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю"]
    # 0123456789
    # qawsasdwew
    not_lazy = True
    for l in layouts:
        for i in range(len(l) - 2):
            # print(l[i:i+3])
            if l[i:i+3] in s:
                not_lazy = False
    
    if not not_lazy:
        raise SequenceError("you're lazy")

    if not any(char.isdigit() for char in s):
        raise DigitError("no digits")
    
    if not any(char.isupper() for char in s):
        raise LetterError("no uppercase characters")
        
    if not any(char.islower() for char in s):
        raise LetterError("no lowercase characters")
    
    if not len(s) > 8:
        raise LengthError("insuffiscient length")

    return 'ok'


if __name__ == "__main__":
    while True:
        pw = input("> ")
        try:
            print(check_password(pw))
        except PasswordError as e:
            print(e)