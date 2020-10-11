class Logic:
    def to_str(self, data):
        if isinstance(data, str):
            return data
        elif isinstance(data, bytes):
            return data.decode("utf-8")
        else:
            raise TypeError(f"Must supply str or bytes, found: {data!r}")


from unittest.mock import Mock

mock_logic = Mock(spec=Logic)
mock_logic.to_str.return_value = "hogehoge"
print(mock_logic.to_str())
