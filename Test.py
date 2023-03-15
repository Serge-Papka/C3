# Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
# унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.

class NonPositiveDigitException(ValueError):
    pass
print(__name__,123)

class Square:
    def __init__(self, a):
        try:
            side = a
            if a <= 0:
                raise NonPositiveDigitException("Ошибкa, a <= 0")
        finally:
            pass


def ttt():
    # print(__name__)
    return 555
    pass

# sq = Square(-1)

