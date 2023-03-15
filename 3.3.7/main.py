"""Вам нужно написать два модуля:
Первый должен содержать число Пи в виде константы 3.14, и две функции, которые будут считать площадь круга и
прямоугольника.
Второй модуль должен импортировать первый, далее запрашивать у пользователя размеры круга и квадрата. В результате
выводить, какая из фигур больше."""

square1 = int(input("Введите сторону квадрата :"))
circle1 = int(input("Введите радиус круга :"))
if Pi_func.circle_area(circle1) > Pi_func.rectangle_area(square1, square1):
    print("площадь круга больше", Pi_func.circle_area(circle1), Pi_func.rectangle_area(square1, square1))
else:
    print("площадь прямоугольника больше", Pi_func.circle_area(circle1), Pi_func.rectangle_area(square1, square1))

