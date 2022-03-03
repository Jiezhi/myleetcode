#!/usr/bin/env python
"""
CREATED AT: 2022/3/3
Des:

https://leetcode.com/problems/evaluate-reverse-polish-notation/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Runtime: 167 ms, faster than 6.50%
        Memory Usage: 14.4 MB, less than 50.42%

        1 <= tokens.length <= 10^4
        tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
        """
        if len(tokens) == 1:
            return int(tokens[0])
        operators = ["+", "-", "*", "/"]
        dq = collections.deque()
        for token in tokens:
            if token in operators:
                num2, num1 = dq.pop(), dq.pop()
                if token == '+':
                    dq.append(num1 + num2)
                elif token == '-':
                    dq.append(num1 - num2)
                elif token == '*':
                    dq.append(num1 * num2)
                elif token == '/':
                    ret = num1 / num2
                    dq.append(math.floor(ret) if ret >= 0 else math.ceil(ret))
            else:
                dq.append(int(token))
        return dq.pop()


def test():
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22


if __name__ == '__main__':
    test()
