#!/usr/bin/env python
"""
CREATED AT: 2022/3/15
Des:

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Runtime: 124 ms, faster than 75.20%
        Memory Usage: 15.8 MB, less than 52.38%

        1 <= s.length <= 10^5
        s[i] is either'(' , ')', or lowercase English letter.
        """
        l = list(s)
        left_pos = []
        for i in range(len(l)):
            if l[i] == '(':
                left_pos.append(i)
            elif l[i] == ')':
                if left_pos:
                    left_pos.pop()
                else:
                    l[i] = ''

        for pos in left_pos:
            l[pos] = ''

        return ''.join(l)


def test():
    assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert Solution().minRemoveToMakeValid("))(") == ""


if __name__ == '__main__':
    test()
