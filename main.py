

def add(a: int, b: int) -> int:
    return a + b


def minus(a: int, b: int) -> int:
    """Функция проверяет разность"""
    return a - b


def divide(a: int, b: int) -> float:
    if b != 0:
        return a / b
    else:
        return 'Делить на ноль нельзя'

print(divide(4, 0))