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
    if has_digits(pw) and \
       has_lowercase(pw) and \
       has_uppercase(pw) and \
       has_length(pw) and \
       not_lazy(pw):
           print("ok")
    else:
        print("error")