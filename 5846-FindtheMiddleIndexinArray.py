#!/usr/bin/env python
"""
CREATED AT: 2021/9/4
Des:
https://leetcode.com/contest/biweekly-contest-60/problems/find-the-middle-index-in-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 
"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        right_sum = sum(nums) - nums[0]
        left_sum = 0
        if right_sum == left_sum:
            return 0
        for i in range(1, len(nums)):
            right_sum -= nums[i]
            left_sum += nums[i - 1]
            if left_sum == right_sum:
                return i
        return -1


def test():
    assert Solution().findMiddleIndex(nums=[2, 3, -1, 8, 4]) == 3
    assert Solution().findMiddleIndex(nums=[1, -1, 4]) == 2
    assert Solution().findMiddleIndex(nums=[2, 5]) == -1
    assert Solution().findMiddleIndex(nums=[1]) == 0


if __name__ == '__main__':
    test()
