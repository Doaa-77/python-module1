
def encrypt(text):
    encrypted = ""

    for character in text:
        encrypted = character + encrypted

    return encrypted


print(encrypt("HELLO"))
