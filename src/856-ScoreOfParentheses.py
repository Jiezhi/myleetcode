#!/usr/bin/env python
"""
CREATED AT: 2022/3/17
Des:
https://leetcode.com/problems/score-of-parentheses/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Runtime: 38 ms, faster than 65.32%
        Memory Usage: 14 MB, less than 30.17%

        2 <= s.length <= 50
        s consists of only '(' and ')'.
        s is a balanced parentheses string.
        """
        if not s:
            return 0

        if len(s) == 2:
            return 1

        if s[1] == ')':
            return 1 + self.scoreOfParentheses(s[2:])

        # s[1] == '(' find the right part of the first (
        left = 1
        for i in range(1, len(s)):
            c = s[i]
            if c == ')':
                left -= 1
                if left == 0:
                    right_pos = i
                    break
            else:
                left += 1

        return 2 * self.scoreOfParentheses(s[1:right_pos]) + self.scoreOfParentheses(s[right_pos + 1:])


def test():
    assert Solution().scoreOfParentheses("(()(()))") == 6
    assert Solution().scoreOfParentheses("()") == 1


if __name__ == '__main__':
    test()
