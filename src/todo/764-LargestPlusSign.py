#!/usr/bin/env python
"""
CREATED AT: 2021/9/9
Des:
https://leetcode.com/problems/largest-plus-sign
https://leetcode.com/explore/item/3969
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        pass


def test():
    assert Solution().orderOfLargestPlusSign(n=5, mines=[[4, 2]]) == 2
    assert Solution().orderOfLargestPlusSign(n=1, mines=[[0, 0]]) == 0
    assert Solution().orderOfLargestPlusSign(n=2, mines=[]) == 1


if __name__ == '__main__':
    test()
