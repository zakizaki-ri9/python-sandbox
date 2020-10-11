class Sample:
    def __init__(self):
        self.x = 1
        self.y = "2"
        self.z = 3.3
        self.xyz = [self.x, self.y, self.z]
        self.xyz_obj = {"x": self.x, "y": self.y, "z": self.z}

    def __repr__(self):
        return f"{self.x!r}, {self.y!r}, {self.z!r}, {self.xyz!r}, {self.xyz_obj!r}"


print(Sample())
