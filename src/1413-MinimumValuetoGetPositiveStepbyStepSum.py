#!/usr/bin/env python
"""
CREATED AT: 2021/11/11
Des:

https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        Runtime: 32 ms, faster than 73.73%
        Memory Usage: 14.1 MB, less than 92.09%

        1 <= nums.length <= 100
        -100 <= nums[i] <= 100
        :param nums:
        :return:
        """
        sum = 0
        min_sum = 0
        for num in nums:
            sum += num
            min_sum = min(sum, min_sum)

        return 1 - min_sum


def test():
    assert Solution().minStartValue(nums=[-3, 2, -3, 4, 2]) == 5
    assert Solution().minStartValue(nums=[1, 2]) == 1
    assert Solution().minStartValue(nums=[1, 2, -5]) == 3
    assert Solution().minStartValue(nums=[1, -2, -3]) == 5


if __name__ == '__main__':
    test()
