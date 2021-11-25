#!/usr/bin/env python
"""
Created on 2018-11-14
Updated on 2021-11-25

Github: https://github.com/Jiezhi/myleetcode

https://leetcode.com/problems/maximum-subarray/description/

@author: 'Jiezhi.G@gmail.com'

Difficulty: Easy
Reference: 
"""
from typing import List


class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        """
        Updated on 2021-11-25

        Runtime: 720 ms, faster than 78.96%
        Memory Usage: 28.8 MB, less than 33.13%
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        :param nums:
        :return:
        """
        last_max_sum = nums[0]
        ret = last_max_sum
        for num in nums[1:]:
            if last_max_sum < 0:
                last_max_sum = num
            else:
                last_max_sum += num
            ret = max(ret, last_max_sum)
        return ret

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
    assert Solution().maxSubArray2(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray2(nums=[5, 4, -1, 7, 8]) == 23


if __name__ == '__main__':
    test()
