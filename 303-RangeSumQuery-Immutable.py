#!/usr/bin/env python
"""
CREATED AT: 2021/8/16
Des:
https://leetcode.com/problems/range-sum-query-immutable/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3892/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections
import itertools
from typing import List


class NumArray:
    """
    15 / 15 test cases passed.
    Status: Accepted
    Runtime: 1100 ms
    Memory Usage: 17.7 MB
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


class NumArray2:
    """

    """

    def __init__(self, nums: List[int]):
        self.accum = list(itertools.accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        return self.accum[right + 1] - self.accum[left]


def test():
    na = NumArray(nums=[-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3

    na = NumArray2(nums=[-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3


if __name__ == '__main__':
    test()
