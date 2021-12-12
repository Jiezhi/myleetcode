#!/usr/bin/env python
"""
CREATED AT: 2021/12/12
Des:
https://leetcode.com/problems/sum-of-subarray-ranges
https://leetcode.com/contest/weekly-contest-271/problems/sum-of-subarray-ranges/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 10 min
"""
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 1000
        -10^9 <= nums[i] <= 10^9
        :param nums:
        :return:
        """
        if len(nums) <= 1:
            return 0
        ret = 0
        for i in range(len(nums) - 1):
            tmp_max = 0
            max_value = nums[i]
            min_value = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > max_value:
                    max_value = nums[j]
                elif nums[j] < min_value:
                    min_value = nums[j]
                tmp_max = max(tmp_max, abs(max_value - min_value))
                ret += tmp_max
        return ret


def test():
    assert Solution().subArrayRanges(nums=[1, 2, 3]) == 4
    assert Solution().subArrayRanges(nums=[1, 3, 3]) == 4
    assert Solution().subArrayRanges(nums=[4, -2, -3, 4, 1]) == 59


if __name__ == '__main__':
    test()
