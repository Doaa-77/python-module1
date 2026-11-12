
file = open("address.txt", "r")
lines = file.readlines()
file.close()

address = lines[2]

word_count = len(address.split())

file = open("address.txt", "a")
file.write("Word count: " + str(word_count) + "\n")
file.close()

print("Word count:", word_count)
