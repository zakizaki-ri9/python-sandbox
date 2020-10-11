class Logic:
    @classmethod
    def to_str(cls, data):
        if isinstance(data, str):
            return data
        elif isinstance(data, bytes):
            return data.decode("utf-8")
        else:
            raise TypeError(f"Must supply str or bytes, found: {data!r}")


from unittest import TestCase, main


class LogicTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual("hello", Logic.to_str(b"hello"))

    def test_to_str_str(self):
        self.assertEqual("hell", Logic.to_str("hell"))

    def test_tostr_bad(self):
        self.assertRaises(TypeError, Logic.to_str, object())


# エラーメッセージは
# assert より TestCase::assertEqual のほうがわかりやすい
class AssertTestCase(TestCase):
    def setUp(self) -> None:
        self.expected = 10

    def test_assert_helper(self):
        # self.expected = 12
        found = 2 * 5
        self.assertEqual(self.expected, found)

    def test_assert_statement(self):
        # self.expected = 12
        found = 2 * 5
        assert self.expected == found


# subTestを用いることで、
# エラーをスルーし、すべてのデータの検証およびエラー内容が確認できる
class DataDrivenTestCase(TestCase):
    def test_good(self):
        good_cases = [
            (b"my bytes", "my bytes"),
            ("no error", b"no error"),  # 失敗ケース
            ("aaa", "bbb"),  # 失敗ケース
            ("other str", "other str"),
        ]
        for value, expected in good_cases:
            with self.subTest(value):
                self.assertEqual(expected, Logic.to_str(value))


if __name__ == "__main__":
    main()
