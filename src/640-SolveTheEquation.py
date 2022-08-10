#!/usr/bin/env python3
"""
CREATED AT: 2022-08-10

URL: https://leetcode.com/problems/solve-the-equation/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 640-SolveTheEquation

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        Runtime: 44 ms, faster than 61.31%
        Memory Usage: 13.9 MB, less than 87.44%

        3 <= equation.length <= 1000
        equation has exactly one '='.
        equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
        return "No solution" or "Infinite solutions" or "x=#"
        """
        left, right = equation.split('=')

        def parse(s: str) -> (int, int):
            co = 0
            num = 0
            pre = 0
            # for convenient
            if s[0] not in ('-', '+'):
                s = '+' + s
            s += '+'
            for pos, x in enumerate(s):
                if x == 'x':
                    if pre == pos:
                        co += 1
                    else:
                        if pre + 1 == pos:
                            co += int(f'{s[pre:pos]}1')
                        else:
                            co += int(s[pre:pos])
                    pre = pos + 1
                elif x in ('-', '+'):
                    if pre != pos:
                        num += int(s[pre:pos])
                        pre = pos

            return co, num

        lco, lnum = parse(left)
        rco, rnum = parse(right)
        co, num = lco - rco, rnum - lnum
        if co == 0 and num != 0:
            return "No solution"
        if co == 0 and num == 0:
            return "Infinite solutions"
        return f'x={num // co}'


def test():
    assert Solution().solveEquation(equation="2x+3x-6x=x+2") == "x=-1"
    assert Solution().solveEquation(equation="x+5-3+x=6+x-2") == "x=2"
    assert Solution().solveEquation(equation="x=x") == "Infinite solutions"
    assert Solution().solveEquation(equation="x=1+x") == "No solution"
    assert Solution().solveEquation(equation="x=-x") == "x=0"
    assert Solution().solveEquation(equation="2x=x") == "x=0"


if __name__ == '__main__':
    test()
