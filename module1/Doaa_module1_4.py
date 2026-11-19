from datetime import datetime


# function to return date, time in order ("%S:%M:%H , %d/%m/%Y")
def get_today_date():
    today = datetime.now()
    return today.strftime("%S:%M:%H , %d/%m/%Y")
print(get_today_date())

# Fibonacci sequence: min and multiple it by 2
def fibonacci_sequence():
    current_minute = datetime.now().minute
    number_of_terms = 2 * current_minute

    sequence = []
    a, b = 0, 1

    for i in range(number_of_terms):
        sequence.append(a)
        a, b = b, a + b

    return sequence
print(fibonacci_sequence())
