from typing import List


def sort_priority(values: List[int], group: set) -> bool:
    found = False

    def helper(x: int) -> (int, int):  # type: ignore
        nonlocal found  # nonlocalを宣言することで、クロージャ内のfoundが、helper以外で定義された変数と認識する
        print(f"x: {x}")
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found


numbers = [1, 3, 8, 9, 2, 5]
group = {2, 3, 5, 7}
found = sort_priority(numbers, group)
print(f"sorted numbers: {numbers}, found: {found}")
