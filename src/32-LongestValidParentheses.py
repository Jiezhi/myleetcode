#!/usr/bin/env python
"""
CREATED AT: 2022/3/24
Des:
https://leetcode.com/problems/longest-valid-parentheses/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        AC: 05/07/2022
        Runtime: 61 ms, faster than 52.96%
        Memory Usage: 14.2 MB, less than 68.41%

        0 <= s.length <= 3 * 10^4
        s[i] is '(', or ')'.
        """
        stack = []
        ret = 0
        tmp_ret = 0
        for c in s:
            if c == '(':
                stack.append(tmp_ret)
                tmp_ret = 0
            elif stack:
                tmp_ret += 2 + stack.pop()
            else:
                # ) and no left parenthesis
                ret = max(tmp_ret, ret)
                tmp_ret = 0

        if stack:
            ret = max(ret, max(stack))
        return max(ret, tmp_ret)


def test():
    assert Solution().longestValidParentheses("(()") == 2
    assert Solution().longestValidParentheses(")()())") == 4
    assert Solution().longestValidParentheses("()(())") == 6


if __name__ == '__main__':
    test()
