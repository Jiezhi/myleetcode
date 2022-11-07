#!/usr/bin/env python3
"""
CREATED AT: 2022-11-07

URL: https://leetcode.com/problems/ambiguous-coordinates/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 816-AmbiguousCoordinates

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        """
        Runtime: 49 ms, faster than 95.41%
        Memory Usage: 14 MB, less than 55.05%
        4 <= s.length <= 12
        s[0] == '(' and s[s.length - 1] == ')'.
        The rest of s are digits.
        """

        def valid(s: str) -> List:
            if len(s) == 1:
                return [s]
            if s[-1] == '0' and s[0] == '0':
                return []
            elif s[0] == '0':
                return [f"{s[0]}.{''.join(s[1:])}"]
            elif s[-1] == '0':
                return [s]
            else:
                return [s] + [f"{''.join(s[:i])}.{''.join(s[i:])}" for i in range(1, len(s))]

        s = list(s)[1:-1]
        ret = []
        for i in range(1, len(s)):
            l, r = valid(''.join(s[:i])), valid(''.join(s[i:]))
            if l and r:
                for a in l:
                    for b in r:
                        ret.append(f"({a}, {b})")
        return ret


def test():
    ans = ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]
    ret = Solution().ambiguousCoordinates(s="(123)")
    assert equal_list_value(ans, ret)

    ans = ["(0, 1.23)", "(0, 12.3)", "(0, 123)", "(0.1, 2.3)", "(0.1, 23)", "(0.12, 3)"]
    ret = Solution().ambiguousCoordinates(s="(0123)")
    assert equal_list_value(ans, ret)

    assert Solution().ambiguousCoordinates(s="(00011)") == ["(0, 0.011)", "(0.001, 1)"]


if __name__ == '__main__':
    test()
