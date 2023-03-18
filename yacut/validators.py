import string


def letters_validator(obj: string) -> bool:
    if obj is not None:
        letters_and_digits = string.ascii_letters + string.digits
        if len(obj) >= 16:
            return False
        for i in obj:
            if i not in letters_and_digits:
                return False
    return True
