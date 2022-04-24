#!/usr/bin/env python
"""
CREATED AT: 2022/4/24
Des:
https://leetcode.com/problems/backspace-string-compare/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Runtime: 38 ms, faster than 64.11%
        Memory Usage: 13.9 MB, less than 77.52%
        if want O(1) space, use two pointers scan from end to beginning.
        1 <= s.length, t.length <= 200
        s and t only contain lowercase letters and '#' characters.
        """
        source_stack = []
        target_stack = []
        for c in s:
            if c == '#' and source_stack:
                source_stack.pop()
            elif c != '#':
                source_stack.append(c)
        for c in t:
            if c == '#' and target_stack:
                target_stack.pop()
            elif c != '#':
                target_stack.append(c)
        return source_stack == target_stack


def test():
    assert Solution().backspaceCompare("ab#c", "ad#c")
    assert Solution().backspaceCompare("y#fo##f", "y#f#o##f")


if __name__ == '__main__':
    test()
