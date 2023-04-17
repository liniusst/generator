# Create a generator function that takes a positive integer n as input
# and generates all the even numbers up to and including n.
# pylint: disable= missing-docstring
from collections.abc import Iterator


def even_number_generator(positive_integer: int) -> Iterator[int]:
    for number in range(positive_integer + 1):
        if positive_integer % 2 == 0:
            yield number


given_number = int(input("Input positive number: "))
generator = even_number_generator(given_number)

for even_number in generator:
    print(f"Number {even_number} is even")
