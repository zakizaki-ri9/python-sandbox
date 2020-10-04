from typing import List


def insertion_sort(data: List[int]) -> List[int]:
    result: List[int] = []
    for value in data:
        insert_value(result, value)
    return result


def insert_value(array: List[int], value: int):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


from random import randint

max_size = 10 ** 4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

from cProfile import Profile

profiler = Profile()
profiler.runcall(test)

from pstats import Stats

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats("cumulative")
stats.print_stats()
