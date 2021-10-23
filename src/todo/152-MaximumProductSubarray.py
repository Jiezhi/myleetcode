#!/usr/bin/env python
"""
CREATED AT: 2021/9/29
Des:
https://leetcode.com/problems/maximum-product-subarray/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
Tags: DP
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass


def test():
    assert Solution().maxProduct(nums=[2, 3, -2, 4]) == 6
    assert Solution().maxProduct(nums=[-2, 0, -1]) == 0


if __name__ == '__main__':
    test()
