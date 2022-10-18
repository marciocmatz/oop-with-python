import math


class Triangle:

    def __init__(self, a=0, b=0, c=0) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2.0
        area = math.pow((p * (p - self.a) * (p - self.b) * (p - self.c)), 1/2)
        return area
