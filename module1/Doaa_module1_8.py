# Count words in each address
def word_count():

    # Read the file
    with open("addresses.text.txt", "r") as f:
        data = f.readlines()

    # Count and save words
    with open("addresses.text.txt", "a") as f:
        for line in data:
            details = line.split(",")

            address = details[2]
            count = len(address.split())

            print("Word count:", count)
            f.write("Word count: " + str(count) + "\n")



word_count()