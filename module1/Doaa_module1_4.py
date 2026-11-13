from datetime import datetime


# Exercise 04 - Part 1
def get_today_date():
    today = datetime.now()
    return today.strftime("%S:%M:%H , %d/%m/%Y")


# Exercise 04 - Part 2
def fibonacci_sequence():
    current_minute = datetime.now().minute
    number_of_terms = 2 * current_minute

    sequence = []
    a, b = 0, 1

    for i in range(number_of_terms):
        sequence.append(a)
        a, b = b, a + b

    return sequence


# Demo
print("Today's Date and Time:")
print(get_today_date())

print("Fibonacci Sequence:")
print(fibonacci_sequence())
