import string


def letters_validator(obj):
    if obj is not None:
        letters_and_digits = string.ascii_letters + string.digits
        for i in obj:
            if i not in letters_and_digits:
                print(type(i))
                return False
        if len(obj) >= 16:
            return False
    return True
