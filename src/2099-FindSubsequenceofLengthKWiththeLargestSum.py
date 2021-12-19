#!/usr/bin/env python
"""
CREATED AT: 2021/12/11
Des:

https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum
https://leetcode.com/contest/biweekly-contest-67/problems/find-subsequence-of-length-k-with-the-largest-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List

from src import tool


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        1 <= nums.length <= 1000
        -10^5 <= nums[i] <= 10^5
        1 <= k <= nums.length
        :param nums:
        :param k:
        :return:
        """
        if k == len(nums):
            return nums
        smallest = sorted(nums)[:len(nums) - k]
        for num in smallest:
            nums.pop(nums.index(num))
        return nums


def test():
    assert Solution().maxSubsequence(nums=[2, 1, 3, 3], k=2) == [3, 3]
    assert Solution().maxSubsequence(nums=[-1, -2, 3, 4], k=3) == [-1, 3, 4]
    assert tool.equal_list_value(Solution().maxSubsequence(nums=[3, 4, 3, 3], k=2) == [3, 4])


if __name__ == '__main__':
    test()
