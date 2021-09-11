#!/usr/bin/env python
"""
CREATED AT: 2021/9/11
Des:
https://leetcode.com/problems/excel-sheet-column-title/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        18 / 18 test cases passed.
        Status: Accepted
        Runtime: 16 ms
        Memory Usage: 14.2 MB
        :param columnNumber:
        :return:
        """
        ret = ''
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, l = divmod(columnNumber, 26)
            ret = chr(l + 65) + ret
        return ret


def test():
    assert Solution().convertToTitle(columnNumber=1) == 'A'
    assert Solution().convertToTitle(columnNumber=28) == 'AB'
    assert Solution().convertToTitle(columnNumber=52) == 'AZ'
    assert Solution().convertToTitle(columnNumber=701) == 'ZY'
    assert Solution().convertToTitle(columnNumber=2147483647) == 'FXSHRXW'


if __name__ == '__main__':
    test()
