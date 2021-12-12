#!/usr/bin/env python
"""
CREATED AT: 2021/12/12
Des:

https://leetcode.com/problems/partition-equal-subset-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Runtime: 3324 ms, faster than 18.21% of Python3
        Memory Usage: 14.3 MB, less than 95.12% of Python3
        1 <= nums.length <= 200
        1 <= nums[i] <= 100
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return False
        sum_num = sum(nums)
        # odd sum
        if (sum_num & 1) == 1:
            return False
        half_sum = sum_num // 2
        nums = sorted(nums)
        if nums[-1] > half_sum:
            return False
        if half_sum in nums:
            return True
        for i in range(len(nums)):
            k = i + 1
            while k < len(nums):
                tmp = nums[i]
                for j in range(k, len(nums)):
                    tmp += nums[j]
                    if tmp == half_sum or half_sum - tmp in nums[j + 1:] or half_sum - tmp in nums[:i]:
                        return True
                    if tmp > half_sum:
                        break
                k += 1
        return False


def test():
    assert Solution().canPartition(nums=[14, 9, 8, 4, 3, 2])
    assert Solution().canPartition(nums=[1, 5, 11, 5])
    assert Solution().canPartition(nums=[1, 1, 1, 1, 3, 5])
    assert not Solution().canPartition(nums=[1, 2, 3, 5])


if __name__ == '__main__':
    test()
