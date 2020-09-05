import itertools
from itertools import zip_longest

# イテレータを繋げる
print(list(itertools.chain([1, 2, 3], [4, 5, 6])))

# 指定回数繰り返し
print(list(itertools.repeat([1, 2, 3], 3)))

# 要素を何回も繰り返す
print([next(itertools.cycle([1, 2])) for _ in range(10)])

# イテレータを指定数作成する
it1, it2, it3 = itertools.tee(["a", "bc"], 3)
print(f"it1={list(it1)}, it2={list(it2)}, it3={list(it3)}")

# 長さが異なるイテレータの場合、終了したら指定した値を返す
print(f"zip: {list(zip([1, 2], ['a', 'bc', 'def']))}")
print(f"zip_longest: {list(zip_longest([1, 2], ['a', 'bc', 'def'], fillvalue='none'))}")

# 複製でなく、特定位置の要素を取り出すだけ
values = list(range(1, 11))
print(f"first five={list(itertools.islice(values, 5))}")
print(f"middle odds={list(itertools.islice(values, 2, 8, 2))}")

# 条件がFalseになるまでイテレータを回し続ける
print(list(itertools.takewhile((lambda x: x < 7), values)))

# 条件がTrueになるまでイテレータをスキップさせる
print(list(itertools.dropwhile((lambda x: x < 7), values)))

# 条件がFalseとなる要素を全て返す
print(f"filter={list(filter((lambda x: x % 2 == 0), values))}")
print(f"filter false={list(itertools.filterfalse((lambda x: x % 2 == 0), values))}")
