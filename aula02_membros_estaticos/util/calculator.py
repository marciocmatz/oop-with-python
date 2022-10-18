
class Calculator:

    @staticmethod
    def circumference(radius: float) -> float:
        PI = 3.14159
        return 2.0 * PI * radius

    @staticmethod
    def volume(radius: float) -> float:
        PI = 3.14159
        return (4.0 * PI * radius * radius * radius) / 3.0
