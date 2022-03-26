#!/usr/bin/env python
"""
CREATED AT: 2022/3/26
Des:
https://leetcode.com/problems/baseball-game/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        """
        Runtime: 44 ms, faster than 83.82%
        Memory Usage: 14.2 MB, less than 38.37%

        :param ops:
        :return:
        """
        stack = []
        for op in ops:
            if op in ['+', 'C', 'D']:
                if op == '+':
                    stack.append(stack[-1] + stack[-2])
                elif op == 'C':
                    stack.pop()
                elif op == 'D':
                    stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)


def test():
    assert Solution().calPoints(["5", "2", "C", "D", "+"]) == 30


if __name__ == '__main__':
    test()
