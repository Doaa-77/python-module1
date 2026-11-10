import os

# Exercise 07 - What It Hides

def count_address_words():

    # Find the file in the same folder
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "addresses.text")

    # Read the address file
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    address_counts = []

    # Count words in each address
    for line in lines:
        if line.startswith("Address:"):
            address = line.split(":", 1)[1].strip()
            word_count = len(address.split())
            address_counts.append(word_count)

    # Append word counts to the same file
    with open(file_path, "a", encoding="utf-8") as file:
        for count in address_counts:
            file.write(f"Address Word Count: {count}\n")

    return address_counts


# Demo
result = count_address_words()
print("Address word counts:", result)
