# TASK: Вычислить колличество N-значных счастливых билетов.
# Счастливым считается билет, если сумма первой половины его цифр равна сумме второй.


def count_tickets(num: int) -> int:
    """Кол-во счастливых билетов в "N" значном диапазоне.
    Билет считается счастливым если первая половина его цифр равна второй.
    Только билеты с четным колличеством символов могут быть счастливыми.
    Билеты с нечетным колличеством символов идентичны, по колличеству счастливых,
    четным, порядком ниже на 1 символ. Билеты, где N < 2 не могут быть счастливыми.

    Example:
    >>>count_tickets(6)
    >>>55252
    """

    temp= {}
    # Получаем половину элементов заданной длинны диапазона.
    for elem in range(int('0' + '9' * (num // 2)) + int(num > 1)):
        # Сумма этих элементов.
        index = sum(map(int, str(elem)))
        # Колличество идентичных сумм.
        temp[index] = temp.get(index, 0) + 1
    # Сумма количеств совпадений 2-х половин числа.
    return sum(i ** 2 for i in temp.values())


if __name__ == '__main__':
    assert count_tickets(2) == 10
    assert count_tickets(4) == 670
    assert count_tickets(6) == 55252