#!/usr/bin/env python3
"""
CREATED AT: 2022-11-13

URL: https://leetcode.com/problems/custom-sort-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 791-CustomSortString

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Runtime: 59 ms, faster than 45.64%
        Memory Usage: 13.8 MB, less than 98.17%

        1 <= order.length <= 26
        1 <= s.length <= 200
        order and s consist of lowercase English letters.
        All the characters of order are unique.
        """
        o = {c: i for i, c in enumerate(order)}
        s = sorted([o[c] if c in o else -1, c] for c in s)
        return ''.join(c[1] for c in s)


def test():
    assert Solution().customSortString(order="cbafg", s="abcd") == "dcba"


if __name__ == '__main__':
    test()
