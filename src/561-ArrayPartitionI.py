#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/8/28

Leetcode: https://leetcode.com/problems/array-partition-i/

"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


def test():
    assert Solution().arrayPairSum([1, 4, 3, 2]) == 4


if __name__ == '__main__':
    test()
