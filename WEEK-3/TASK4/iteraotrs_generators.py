import random

class Countdown:
    """Iterator class that counts down from a given number to 1."""
    def __init__(self, start):
        if start < 1:
            raise ValueError("Start must be at least 1.")
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        current_value = self.current
        self.current -= 1
        return current_value


def fibonacci_generator(limit):
    """Generator function that yields Fibonacci numbers up to a specified limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def random_number_generator(start, end, count):
    """Generator function that yields a sequence of random numbers between a specified range."""
    if start > end:
        raise ValueError("Start should be less than or equal to end.")
    for _ in range(count):
        yield random.randint(start, end)


def main():
   
    print("Countdown from 5:")
    try:
        for number in Countdown(5):
            print(number, end=" ")
    except ValueError as e:
        print("Error:", e)
    print("\n")

   
    print("Fibonacci numbers up to 20:")
    for number in fibonacci_generator(20):
        print(number, end=" ")
    print("\n")

    
    print("Random numbers between 1 and 10:")
    for number in random_number_generator(1, 10, 5):
        print(number, end=" ")
    print("\n")


if __name__ == "__main__":
    main()
