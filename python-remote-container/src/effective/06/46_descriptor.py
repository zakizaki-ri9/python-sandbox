class Grade:

    MIN = 0
    MAX = 100
    _value: int

    def __init__(self) -> None:
        self._value = self.MIN

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (self.MIN <= value <= self.MAX):
            raise ValueError(f"Grade must be between {self.MIN} and {self.MAX}")
        self._value = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

    def output(self):
        return f"math_grade={self.math_grade}, writing_grade={self.writing_grade}, science_grade={self.science_grade}"


first_exam = Exam()
first_exam.math_grade = 1
first_exam.writing_grade = 82
first_exam.science_grade = 99
print(first_exam.output())

first_exam.science_grade = -1