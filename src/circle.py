from src.figure import Figure
import math
PI = 3.14

class Circle(Figure):
    def __init__(self, radius: int):
        self.name = 'Circle'
        self.radius = radius
        self.check_if_can_create_circle(radius)

    def get_area(self) -> float:
        area = self.radius ** 2 * PI
        return round(area, 2)

    def get_perimeter(self) -> float:
        perimeter = self.radius * 2 * PI
        return round(perimeter, 2)

    @staticmethod
    def check_if_can_create_circle(radius: int):
        if radius > 0:
            return radius
        else:
            raise ValueError('The input numbers should be positive')
