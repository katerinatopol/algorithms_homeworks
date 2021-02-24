"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
import cProfile
from random import randint
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def revers_test(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def main():
    revers_1(num)
    revers_2(num)
    revers_3(num)
    revers_test(num)


num = randint(10000, 1000000)

print(
    timeit(
        'revers_1(num)',
        setup='from __main__ import revers_1, num',
        number=10000))
print(
    timeit(
        'revers_2(num)',
        setup='from __main__ import revers_2, num',
        number=10000))
print(
    timeit(
        'revers_3(num)',
        setup='from __main__ import revers_3, num',
        number=10000))
print(
    timeit(
        'revers_test(num)',
        setup='from __main__ import revers_test, num',
        number=10000))


cProfile.run('main()')

"""
Время работы:
0.046865199999999996
0.03401309999999999
0.009548100000000004

0.00542910000000002

Оптимальный вариант из предложенных - 3. Первая функция использует рекурсию, вторая цикл - поэтому они работают 
медленнее третьего варианта, где использован срез. В качестве своего варианта попробовала мемоизацию рекурсии, по 
результатам она работает лучше всего.
"""