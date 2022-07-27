#!/usr/bin/env python3
"""
CREATED AT: 2022-07-27

URL: https://leetcode.com/problems/fraction-addition-and-subtraction/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 592-FractionAdditionAndSubtraction

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def fractionAddition(self, expression: str) -> str:
        """
        Runtime: 49 ms, faster than 48.44% 
        Memory Usage: 13.9 MB, less than 41.33% 

        The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
        Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
        The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
        The number of given fractions will be in the range [1, 10].
        The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
        """
        expression += '+'
        a, b, c, d = 0, 1, None, None
        pre = 0
        for i, e in enumerate(expression):
            if e == '-' or e == '+':
                if c is None:
                    # begin of c
                    pass
                else:
                    # end of d
                    d = int(expression[pre:i])
                    pre = i
                    a, b, c, d = a * d + b * c, b * d, None, None
                    g = math.gcd(a, b)
                    if g != 1:
                        a, b = a // g, b // g
            elif e == '/':
                c = int(expression[pre:i])
                pre = i + 1
        return f'{a}/{b}'


def test():
    assert Solution().fractionAddition(expression="-1/2+1/2") == "0/1"
    assert Solution().fractionAddition(expression="-1/2+1/2+1/3") == "1/3"
    assert Solution().fractionAddition(expression="1/3-1/2") == "-1/6"


if __name__ == '__main__':
    test()
