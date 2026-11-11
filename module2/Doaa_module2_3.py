def unique_numbers(numbers):

    unique = []

    for number in numbers:

        if number not in unique:
            unique.append(number)

    return unique


print(unique_numbers([1, 2, 2, 3, 4, 4, 5]))