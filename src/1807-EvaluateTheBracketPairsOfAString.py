#!/usr/bin/env python3
"""
CREATED AT: 2023-01-15

URL:

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1807-EvaluateTheBracketPairsOfAString

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dct = {k: v for k, v in knowledge}
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                tmp = ''.join(tmp[::-1])
                stack.append(dct.get(tmp, '?'))
        return ''.join(stack)


def test():
    assert Solution().evaluate(s="(name)is(age)yearsold",
                               knowledge=[["name", "bob"], ["age", "two"]]) == "bobistwoyearsold"


if __name__ == '__main__':
    test()
