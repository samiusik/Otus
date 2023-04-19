import pytest
from src.circle import Circle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize('radius, expected_perimeter, expected_area',
                         [
                             (10, 62.8, 314),
                             (2, 12.56, 12.56),
                             (5, 31.4, 78.5),
                         ]
                         )
def test_circle_creation_positive(radius, expected_perimeter, expected_area):
    circle = Circle(radius)
    assert circle.name == 'Circle', 'Expected name is Triangle'
    assert circle.get_perimeter() == expected_perimeter, 'Expected correct perimeter'
    assert circle.get_area() == expected_area, 'Expected correct area'


@pytest.mark.parametrize('radius',
                         [
                             0,
                             -2
                         ],
                         ids=[
                             'radius side is zero',
                             'radius side is negative'
                         ])
def test_circle_creation_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_two_circle_areas_sum():
    expected_sum = 326.56
    circle_1 = Circle(10)
    circle_2 = Circle(2)
    assert circle_1.add_area(circle_2) == expected_sum, f'Expected sum is {expected_sum}'


def test_circle_and_square_areas_sum():
    expected_sum = 16.56
    square = Square(2)
    circle = Circle(2)
    assert square.add_area(circle) == expected_sum, f'Expected sum is {expected_sum}'


def test_circle_and_triangle_areas_sum():
    expected_sum = 55.86
    triangle = Triangle(10, 10, 10)
    circle = Circle(2)
    assert triangle.add_area(circle) == expected_sum, f'Expected sum is {expected_sum}'
