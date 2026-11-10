
def speaking_is_expensive(text, price_per_letter):

    shifted_string = ""

    # Shift each letter by one
    for letter in text:
        if letter.isalpha():
            if letter == "z":
                shifted_string += "a"
            elif letter == "Z":
                shifted_string += "A"
            else:
                shifted_string += chr(ord(letter) + 1)
        else:
            shifted_string += letter

    # Count words
    word_count = len(text.split())

    # Count letters only
    letter_count = sum(1 for letter in text if letter.isalpha())

    # Calculate price
    total_price = letter_count * price_per_letter

    # Return results in dictionary format
    return {
        "shifted_string": shifted_string,
        "word_count": word_count,
        "price": total_price
    }


# Demo
text = "speaking is expensive"
price_per_letter = 2

result = speaking_is_expensive(text, price_per_letter)

print(result)
