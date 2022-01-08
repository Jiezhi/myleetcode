#!/usr/bin/env python
"""
CREATED AT: 2022/1/8
Des:

https://leetcode.com/problems/gray-code/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        pass


def test():
    assert Solution().grayCode(1) == [0, 1]
    assert Solution().grayCode(2) in [[0, 1, 3, 2], [0, 2, 3, 1]]


if __name__ == '__main__':
    test()
