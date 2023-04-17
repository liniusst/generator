# pylint: disable= missing-docstring

import sys
import time
from collections.abc import Iterator
from typing import List
from py_random_words import RandomWords

r_word = RandomWords()


def generate_random_base_list() -> List[str]:
    base_list = []
    for value in range(15000):
        value = r_word.get_word()
        base_list.append(value)
    return base_list


rnd_word_list = generate_random_base_list()


def generate_random_list() -> Iterator[str]:
    for value in rnd_word_list:
        if len(value) > 7:
            yield value


start_gc = time.time()
random_word_list_gc = generate_random_list()
stop_gc = time.time()

start_lt = time.time()
random_word_list_lt = [word for word in rnd_word_list if len(word) > 7]
stop_lt = time.time()

print(f"Generator list size: {sys.getsizeof(random_word_list_gc)}")
print(f"GC executie time: {(stop_gc - start_gc)} ms")
print(f"List comprehension size: {sys.getsizeof(random_word_list_lt)}")
print(f"LT executie time: {(stop_lt - start_lt)} ms")
