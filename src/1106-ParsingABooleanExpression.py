#!/usr/bin/env python3
"""
CREATED AT: 2022-11-05

URL: https://leetcode.com/problems/parsing-a-boolean-expression/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1106-ParsingABooleanExpression

Difficulty: Hard

Desc: 

Tag: 

See: 

"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        """
        Runtime: 85 ms, faster than 73.11%
        Memory Usage: 14.1 MB, less than 61.79%

        1 <= expression.length <= 2 * 104
        expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
        """
        if expression == 't':
            return True
        if expression == 'f':
            return False
        sub = expression[2:-1]
        if expression[0] == '!':
            return not self.parseBoolExpr(sub)
        elif expression[0] == '|':
            left = 0
            cur = 0
            for i, c in enumerate(sub):
                if c == '(':
                    if left == 0:
                        cur = i - 1
                    left += 1
                elif c == ')':
                    left -= 1
                    if left == 0:
                        if self.parseBoolExpr(sub[cur:i + 1]):
                            return True
                        else:
                            cur = i + 2
                elif left == 0 and c == 't':
                    return True
            return False
        elif expression[0] == '&':
            left = 0
            cur = 0
            for i, c in enumerate(sub):
                if c == '(':
                    if left == 0:
                        cur = i - 1
                    left += 1
                elif c == ')':
                    left -= 1
                    if left == 0:
                        if not self.parseBoolExpr(sub[cur:i + 1]):
                            return False
                        else:
                            cur = i + 2
                elif left == 0 and c == 'f':
                    return False
            return True


def test():
    assert Solution().parseBoolExpr(expression="|(f,f,f,!(f))")
    assert not Solution().parseBoolExpr(expression="&(|(f))")
    assert Solution().parseBoolExpr(expression="|(f,f,f,t)")
    assert Solution().parseBoolExpr(expression="!(&(f,t))")


if __name__ == '__main__':
    test()
