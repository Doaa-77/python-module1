def check_string(value):

    try:
        if isinstance(value, str):
            print(value)
        else:
            return None

    except:
        return None


print("Hello")