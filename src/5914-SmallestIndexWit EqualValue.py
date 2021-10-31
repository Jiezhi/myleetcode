#!/usr/bin/env python
"""
CREATED AT: 2021/10/31
Des:

https://leetcode.com/contest/weekly-contest-265/problems/smallest-index-with-equal-value
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 100
        0 <= nums[i] <= 9
        :param nums:
        :return:
        """
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1


def test():
    assert Solution().smallestEqual(nums=[0, 1, 2]) == 0
    assert Solution().smallestEqual(nums=[2, 1, 3, 5, 2]) == 1
    assert Solution().smallestEqual(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == -1


if __name__ == '__main__':
    test()
