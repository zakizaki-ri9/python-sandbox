class ToDictMixin:
    def to_dict(self):
        return self.__traverse_dict(self.__dict__)

    def __traverse_dict(self, instance_dict: dict):
        output = {}
        for k, v in instance_dict.items():
            output[k] = self.__traverse(k, v)
        return output

    def __traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self.__traverse_dict(value)
        elif isinstance(value, list):
            return [self.__traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            return self.__traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None) -> None:
        init_values = dict(locals())
        del init_values["self"]
        for key, value in init_values.items():
            setattr(self, key, value)


tree = BinaryTree(
    10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)),
)

# print(tree)
print(tree.to_dict())
