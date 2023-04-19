from src.figure import Figure


class Square(Figure):
    def __init__(self, a_side: int):
        self.name = 'Square'
        self.a_side = a_side
        self.check_if_can_create_square(a_side)

    def get_area(self) -> int:
        area = self.a_side ** 2
        return round(area)

    def get_perimeter(self) -> int:
        return self.a_side * 4

    @staticmethod
    def check_if_can_create_square(a_side: int):
        if a_side > 0:
            return a_side
        else:
            raise ValueError('The input numbers should be positive')
