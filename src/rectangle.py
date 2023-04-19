from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a_side: int, b_side: int):
        self.name = 'Rectangle'
        self.a_side = a_side
        self.b_side = b_side
        self.check_if_can_create_rectangle(a_side, b_side)

    def get_area(self) -> int:
        area = self.a_side * self.b_side
        return round(area, 2)

    def get_perimeter(self) -> int:
        perimeter = (self.a_side + self.b_side) * 2
        return round(perimeter, 2)

    @staticmethod
    def check_if_can_create_rectangle(a_side: int, b_side: int):
        if not (a_side > 0 and b_side > 0):
            raise ValueError(f'Sides must be greater than 0. Got: {a_side}, {b_side}')
