#!/usr/bin/env python3
"""
CREATED AT: 2022-11-20

URL: https://leetcode.com/problems/basic-calculator/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 224-BasicCalculator

Difficulty: Hard

Desc: 

Tag: 

See: 

"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        https://leetcode.cn/problems/basic-calculator/solution/ji-ben-ji-suan-qi-by-leetcode-solution-jvir/
        1 <= s.length <= 3 * 105
        s consists of digits, '+', '-', '(', ')', and ' '.
        s represents a valid expression.
        '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
        '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
        There will be no two consecutive operators in the input.
        Every number and running calculation will fit in a signed 32-bit integer.
        """
        ret, sign, i = 0, 1, 0
        ops = [1]
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                i += 1
                sign = ops[-1]
            elif s[i] == '-':
                i += 1
                sign = -ops[-1]
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ret += num * sign
        return ret


def test():
    assert Solution().calculate(s="1 + 1") == 2
    assert Solution().calculate(s=" 2-1 + 2 ") == 3
    assert Solution().calculate(s="(1+(4+5+2)-3)+(6+8)") == 23


if __name__ == '__main__':
    test()
