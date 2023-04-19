import pytest
from src.rectangle import Rectangle
from src.triangle import Triangle
from src.circle import Circle


@pytest.mark.parametrize('side_a, side_b, expected_perimeter, expected_area',
                         [(1, 2, 6, 2),
                          (2, 4, 12, 8),
                          (5, 10, 30, 50)
                          ])
def test_rectangle_creation_positive(side_a, side_b, expected_perimeter, expected_area):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.name == 'Rectangle', 'Expected name is Rectangle'
    assert rectangle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert rectangle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('side_a, side_b',
                         [
                             (0, 1),
                             (-5, 10)
                         ],
                         ids=[
                             'one side is zero',
                             'one side is negative'
                         ])
def test_rectangle_creation_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_two_rectangle_areas_sum():
    expected_sum = 30
    rectangle_1 = Rectangle(10, 2)
    rectangle_2 = Rectangle(2, 5)
    assert rectangle_1.add_area(rectangle_2) == expected_sum, f'Expected sum is {expected_sum}'


def test_circle_and_triangle_areas_sum():
    expected_sum = 55.86
    triangle = Triangle(10, 10, 10)
    circle = Circle(2)
    assert triangle.add_area(circle) == expected_sum, f'Expected sum is {expected_sum}'
