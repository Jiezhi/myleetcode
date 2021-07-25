#!/usr/bin/env python
"""
CREATED AT: 2021/7/25
Des:

https://leetcode.com/contest/weekly-contest-251/problems/largest-number-after-mutating-substring/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ret = ''
        start = False
        end = False
        for n in num:
            if not start:
                if int(n) >= change[int(n)]:
                    ret += n
                else:
                    start = True
                    ret += str(change[int(n)])
            else:
                if not end:
                    if int(n) <= change[int(n)]:
                        ret += str(change[int(n)])
                    else:
                        end = True
                        ret += n
                else:
                    ret += n
        return ret


def test():
    assert Solution().maximumNumber("334111", [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]) == "334999"
    assert Solution().maximumNumber(num="330", change=[9, 3, 6, 3, 7, 3, 1, 4, 5, 8]) == '339'
    assert Solution().maximumNumber(num="132", change=[9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == '832'
    assert Solution().maximumNumber(num="021", change=[9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == '934'
    assert Solution().maximumNumber(num="5", change=[1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == '5'


if __name__ == '__main__':
    test()
