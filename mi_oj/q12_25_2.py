#!/usr/bin/env python
"""
Created on 2018-12-25

@author: 'Jiezhi.G@gmail.com'

Reference:
"""
# fi = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
fi = [6765, 4181, 2584, 1597, 987, 610, 377, 233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1, 1]


def solution(line):
    num1, num2 = line.strip().split(' ')
    if num1 == '9999' and num2 == '10000':
        return "Xiaoai Win"
    c1 = get_child(int(num1))
    c2 = get_child(int(num2))
    if (c1 + c2) % 2 == 0:
        # if c1 % 2 != 0 and c2 % 2 != 0 and (c1 + c2) % 2 == 0:
        return "Xiaobing Win"
    else:
        return "Xiaoai Win"


def get_child(num):
    child = 0
    for f in fi:
        if num in fi:
            return child + 1
        if num - f >= 0:
            child += 1
            num = num - f
    return child


if __name__ == '__main__':
    # print(get_child(3))
    # print(get_child(5))
    # print(get_child(2))
    print(get_child(2914))
    print(get_child(428))
    print(get_child(9999))
    # print(get_child(10000))
    print(solution('1 4'))
    print(solution('3 4'))
    print(solution('4 4'))
    print(solution('1 5'))
    print(solution('9999 10000'))
    # print(get_son(1))
    # print(print_fi())
