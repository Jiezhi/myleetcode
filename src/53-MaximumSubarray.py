#!/usr/bin/env python
"""
Created on 2018-11-14
https://leetcode.com/problems/maximum-subarray/description/

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        tmp_sum = nums[0]
        for i in range(1, len(nums)):
            tmp_sum = max(nums[i], tmp_sum + nums[i])
            max_sum = max(max_sum, tmp_sum)
        return max_sum


def test():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
