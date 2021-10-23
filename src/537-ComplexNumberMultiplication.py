#!/usr/bin/env python
"""
CREATED AT: 2021/8/24
Des:
https://leetcode.com/problems/complex-number-multiplication/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3917/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        55 / 55 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.3 MB
        https://wikimedia.org/api/rest_v1/media/math/render/svg/32ed644695ae41461727e40341172d44093203ec
        (a+bi)(c+di)=ac + bci + adi + dbi^2 = (ac-db)+(bc+ad)i
        :param num1:
        :param num2:
        :return:
        """
        a = num1.split('+')[0]
        b = num1.split('+')[1][:-1]
        c = num2.split('+')[0]
        d = num2.split('+')[1][:-1]
        real = (int(a) * int(c) - int(b) * int(d))
        imaginary = (int(b) * int(c) + int(a) * int(d))
        return f'{real}+{imaginary}i'


def test():
    assert Solution().complexNumberMultiply(num1="1+1i", num2="1+1i") == "0+2i"
    assert Solution().complexNumberMultiply(num1="1+-1i", num2="1+-1i") == "0+-2i"


if __name__ == '__main__':
    test()
