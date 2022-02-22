#!/usr/bin/env python
"""
CREATED AT: 2022/2/22
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent: 2 min
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Runtime: 36 ms, faster than 77.88%
        Memory Usage: 13.9 MB, less than 62.82%
        1 <= columnTitle.length <= 7
        columnTitle consists only of uppercase English letters.
        columnTitle is in the range ["A", "FXSHRXW"].
        """
        pos = 0
        ret = 0
        ord_a = ord('A')
        for i in range(len(columnTitle) - 1, -1, -1):
            ret += (ord(columnTitle[i]) - ord_a + 1) * (26 ** pos)
            pos += 1
        return ret


def test():
    assert Solution().titleToNumber("A") == 1
    assert Solution().titleToNumber("ZY") == 701


if __name__ == '__main__':
    test()
