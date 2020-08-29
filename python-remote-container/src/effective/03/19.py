from typing import List


def get_stats(numbers: List[int]) -> (int, int, int, int, int):  # type: ignore
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum, len(numbers), numbers[0], numbers[-1]


lengths = [1, 3, 5, 9, 2, 8, 6]
# minimum, maximum, first, last, count = get_stats(lengths) のように順番を間違えやすい
minimum, maximum, count, first, last = get_stats(lengths)
print(f"Min: {minimum}, Max: {maximum}, Count: {count}, first: {first}, last: {last}")
