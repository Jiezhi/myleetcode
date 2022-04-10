#!/usr/bin/env python
"""
CREATED AT: 2022/4/10
Des:

https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def minimizeResult(self, expression: str) -> str:
        """
        3 <= expression.length <= 10
        expression consists of digits from '1' to '9' and '+'.
        expression starts and ends with digits.
        expression contains exactly one '+'.
        The original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.
        :param expression:
        :return:
        """
        s = expression
        ret_value = eval(s)
        ret_str = f'({s})'
        lo = 0
        while s[lo] != '+':
            for i in range(len(s) - 1, 0, -1):
                if s[i] == '+':
                    break
                exp = f'{1 if not s[:lo] else s[:lo]}*({s[lo:i + 1]})*{1 if not s[i + 1:] else s[i + 1:]}'
                ret = eval(exp)
                if ret < ret_value:
                    ret_value = ret
                    ret_str = f'{s[:lo]}({s[lo:i + 1]}){s[i + 1:]}'
            lo += 1
        return ret_str


def test():
    assert Solution().minimizeResult(expression="247+38") == "2(47+38)"
    assert Solution().minimizeResult(expression="12+34") == "1(2+3)4"
    assert Solution().minimizeResult(expression="999+999") == "(999+999)"


if __name__ == '__main__':
    test()
