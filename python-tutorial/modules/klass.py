class MyClass:
    """Simple Class"""

    def __init__(self):
        self.member_num = 1
        self.member_str = "test"

    def f(self):
        return {'member_num': self.member_num,  'member_str': self.member_str}
