import os
from typing import Callable, Generator, Iterator, List


class Anti:
    @classmethod
    def get_percentages(cls, data_path: str) -> List[float]:
        it = cls.__read_visits(data_path=data_path)
        percentages = cls.__normalize(it)
        return percentages

    @classmethod
    def __normalize(cls, numbers: Generator[float, None, None]) -> List[float]:
        # このsumでイテレータの結果を生成してしまう
        total = sum(numbers)

        # このforでは、イテレータが終了している
        result = []
        for value in numbers:
            percent = 100 * value / total
            result.append(percent)
        print(f"result={result}")
        return result

    @classmethod
    def __read_visits(cls, data_path: str) -> Generator[float, None, None]:
        with open(data_path) as f:
            for line in f:
                yield float(line)


class Better:
    @classmethod
    def get_percentages(cls, data_path: str) -> List[float]:
        percentages = cls.__normalize(lambda: cls.__read_visits(data_path=data_path))
        return percentages

    @classmethod
    def __normalize(
        cls, get_numbers_iter_func: Callable[[], Iterator[float]]
    ) -> List[float]:
        # イテレータを毎回生成することで、以下を回避
        # ・入力をListとしないことで、パラメータが巨大でメモリクラッシュするのを避ける
        # ・sum, resultを生成する両方のタイミングでイテレータを生成、求める結果を出力する
        total = sum(get_numbers_iter_func())
        result = []
        for value in get_numbers_iter_func():
            percent = 100 * value / total
            result.append(percent)
        return result

    # Anti::__read_visitsと同じく、ジェネレータを返す
    @classmethod
    def __read_visits(cls, data_path: str) -> Generator[float, None, None]:
        with open(data_path) as f:
            for line in f:
                yield float(line)


class ReadVisits:
    def __init__(self, data_path: str):
        self.data_path = data_path

    # 呼び出される or 終了するまで、iteratorが生成 or 回される
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield float(line)


class Best:
    @classmethod
    def get_percentages(cls, data_path: str) -> List[float]:
        visits = ReadVisits(data_path=data_path)
        percentages = cls.__normalize(visits)
        return percentages

    @classmethod
    def __normalize(cls, read_visits: ReadVisits) -> List[float]:
        total = sum(read_visits)
        result = []
        for value in read_visits:
            percent = 100 * value / total
            result.append(percent)
        return result


data_path = os.path.join(os.getcwd(), __file__.replace(".py", ".txt"))

# output: Anti=[] となる
print(f"Anti={Anti.get_percentages(data_path=data_path)}")

# output: Better=[...] となる
print(f"Better={Better.get_percentages(data_path=data_path)}")

# output: Better=[...] となる
print(f"Best={Best.get_percentages(data_path=data_path)}")
