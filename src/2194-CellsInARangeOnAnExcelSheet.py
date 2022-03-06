#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        """
        s.length == 5
        'A' <= s[0] <= s[3] <= 'Z'
        '1' <= s[1] <= s[4] <= '9'
        s consists of uppercase English letters, digits and ':'.
        """
        ret = []

        for c in range(ord(s[0]), ord(s[3]) + 1):
            for r in range(int(s[1]), int(s[4]) + 1):
                ret.append(f'{chr(c)}{r}')
        return ret


def test():
    assert Solution().cellsInRange('A1:C3') == ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    assert Solution().cellsInRange("A1:F1") == ["A1", "B1", "C1", "D1", "E1", "F1"]


if __name__ == '__main__':
    test()
