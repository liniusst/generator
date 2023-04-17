# Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000)
# and would stop itterating
# until the word longer than 7 lettters is found.
# Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms)
# pylint: disable= missing-docstring
import sys
import time
from collections.abc import Iterator
from py_random_words import RandomWords

r_word = RandomWords()


def generate_random_list() -> Iterator[str]:
    for value in range(10000):
        value = r_word.get_word()
        yield value


start_gc = time.time()
random_word_list_gc = generate_random_list()
for word in random_word_list_gc:
    if len(word) > 7:
        break
stop_gc = time.time()


start_lt = time.time()
random_word_list_lt = (r_word.get_word() for _ in range(10000))
for word in random_word_list_lt:
    if len(word) > 7:
        break
stop_lt = time.time()

print(f"Generator list size: {sys.getsizeof(random_word_list_gc)}")
print(f"GC executie time: {(stop_gc - start_gc) * 10**3} ms")
print(f"List comprehension size: {sys.getsizeof(random_word_list_lt)}")
print(f"LT executie time: {(stop_lt - start_lt) * 10**3} ms")
