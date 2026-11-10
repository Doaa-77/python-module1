def accept_string(value):

    try:
        if isinstance(value, str):
            print(value)
            return value
        else:
            return None

    except:
        return None


# Demo
print(accept_string("Hello"))
print(accept_string(123))
print(accept_string(5.5))