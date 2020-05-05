# [Python3.7 チュートリアル](https://docs.python.org/ja/3.7/tutorial/)の素振り

---

# メモ

## モジュール

### import

`fibo.py`をモジュールとして扱える。

```bash
pipenv shell
python

>>> import fibo
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 
>>> fibo.fib(100)
0 1 1 2 3 5 8 13 21 34 55 89 
>>> fibo.__name__
'fibo'
>>> exit()
```

他にも以下のようなimport方法がある。

```python
# モジュールから特定の関数をimport
>>> from fibo import fib, fib2

# _から始まる関数をのぞいて全てのものをimport
>>> from fibo import *

# asで名称変更
>>> import fibo as fib
>>> from fibo import fib as fibonacci
```

### スクリプト実行

```python
if __name__ == "__main__":
  # メイン処理
```

を末尾に記載すると、スクリプトとして実行される。

### パッケージ

- `__init__.py`が定義されていることでパッケージ化が可能となる
- `__all__`に記載することで、`from パッケージ名 import *`で一括impoortが可能となる

