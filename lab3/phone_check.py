class PhoneException(Exception):
    pass

class FormatError(PhoneException):
    pass

class CountError(PhoneException):
    pass

class CountryCodeError(PhoneException):
    pass

class ProviderError(PhoneException):
    pass


def check_number(s):
    if not s.count("(") == s.count(")") or "--" in s:
        raise FormatError("Invalid format")
    
    if not (s[0] == "8" or s[0:2] == "+7"):
        raise CountryCodeError("Invalid country code")
    
    chars = ['-', '+', '(', ')', ' ']
    for c in chars:
        s = s.replace(c, '')
    
    if len(s) != 11:
        raise CountError("Invalid digit count")
    
    s = '7' + s[1:]
    
    return f"+{s}"
    
    


if __name__ == "__main__":
    numbers = [
        "+7(902)123-4567",
        "8(902)1-2-3-45-67",
        "504))635(22))9    9",
        "8--9019876543-22-3--4",
        "87393))985942",
        "9914273   13-87",
        "8846776522",
        "+71113253136",
        "8(916)     12 4 32-6 7"
    ]
    
    for n in numbers:
        try:
            print(check_number(n))
        except PhoneException as e:
            print(e)

