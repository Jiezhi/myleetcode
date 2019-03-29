#!/usr/bin/env python
"""
https://leetcode.com/problems/integer-to-roman/
Created on 2018-12-14

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
              10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
              100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
              1000: 'M'
              }

# Method 2:
roman_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
              (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        for i in [1000, 100, 10, 1]:
            ret, num = divmod(num, i)
            if ret == 0:
                continue
            if ret * i in roman_dict:
                s += roman_dict[ret * i]
            elif ret > 5:
                s += roman_dict[5 * i] + roman_dict[i] * (ret - 5)
            else:
                s += roman_dict[i] * ret
        return s

    def intToRoman2(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        for key, value in roman_list:
            while num >= key:
                s += value
                num -= key
        return s


def compare_test_fun(func):
    assert func(3) == 'III'
    assert func(4) == 'IV'
    assert func(8) == 'VIII'
    assert func(9) == 'IX'
    assert func(58) == 'LVIII'
    assert func(1994) == 'MCMXCIV'


def compare_fun():
    import timeit
    print(timeit.timeit("test(Solution().intToRoman)", setup="from __main__ import test, Solution"))
    print(timeit.timeit("test(Solution().intToRoman2)", setup="from __main__ import test, Solution"))


def test():
    assert Solution().intToRoman(3) == 'III'


if __name__ == '__main__':
    test()
