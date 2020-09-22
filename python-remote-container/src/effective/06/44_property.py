class Resistor:
    def __init__(self, ohms) -> None:
        self._ohms = ohms
        self.voltage = 0.0
        self.current = 0.0


class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


r = MysteriousResistor(10)
r.current = 0.01
print(f"Before: {r.voltage:.2f}")
r.ohms
print(f"After: {r.voltage:.2f}")
r.ohms = 2
print(f"r.ohms = 2 After: {r.voltage:.2f}")
r.ohms
print(f"r.ohms After: {r.voltage:.2f}")
