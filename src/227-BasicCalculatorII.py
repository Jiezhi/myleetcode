#!/usr/bin/env python
"""
CREATED AT: 2022/3/3
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        Runtime: 122 ms, faster than 54.57%
        Memory Usage: 16.1 MB, less than 19.77%

        1 <= s.length <= 3 * 10^5
        s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
        s represents a valid expression.
        All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
        The answer is guaranteed to fit in a 32-bit integer.
        """
        num_stack = []
        operator_stack = []
        num_start_pos = 0
        s = s.replace(' ', '')
        calc_now = False  # if we meet * or /, get the next num and calc it
        for i in range(1, len(s)):
            if s[i] in ['+', '-', '*', '/']:
                next_num = int(s[num_start_pos:i])
                if calc_now:
                    pre_num = num_stack.pop()
                    op = operator_stack.pop()
                    if op == '*':
                        num_stack.append(pre_num * next_num)
                    else:
                        num_stack.append(int(float(pre_num) / next_num))
                    calc_now = False
                else:
                    num_stack.append(next_num)

                operator_stack.append(s[i])
                num_start_pos = i + 1

                if s[i] == '*' or s[i] == '/':
                    calc_now = True
        # process last num and operator
        next_num = int(s[num_start_pos:])
        if calc_now:
            pre_num = num_stack.pop()
            op = operator_stack.pop()
            if op == '*':
                num_stack.append(pre_num * next_num)
            else:
                num_stack.append(int(float(pre_num) / next_num))
        else:
            num_stack.append(next_num)
        # now only "+" and "-" in operator_stack
        i = 0
        ret = num_stack[0]
        while i < len(operator_stack):
            op = operator_stack[i]

            if op == '+':
                ret += num_stack[i + 1]
            else:
                ret -= num_stack[i + 1]
            i += 1
        return ret


def test():
    assert Solution().calculate("3+2*2") == 7
    assert Solution().calculate(" 3/2 ") == 1
    assert Solution().calculate(" 3+5 / 2 ") == 5


if __name__ == '__main__':
    test()
