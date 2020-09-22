class MyBaseClass:
    def __init__(self, value) -> None:
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self) -> None:
        MyBaseClass.__init__(self, 5)


class TimesTwo:
    def __init__(self):
        self.value *= 2


class PlusFive:
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        # MyBaseClass.__init__(self, value)
        # TimesTwo.__init__(self)
        # PlusFive.__init__(self)
        super().__init__(value)


foo = OneWay(5)
print(f"First ordering is (5 * 2) + 5 = {foo.value}")

mro_str = "\n".join(repr(cls) for cls in OneWay.mro())
print(mro_str)