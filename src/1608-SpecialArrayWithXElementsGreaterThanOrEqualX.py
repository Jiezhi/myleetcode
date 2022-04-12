#!/usr/bin/env python
"""
CREATED AT: 2022/4/12
Des:
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag:

See:

"""
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Runtime: 36 ms, faster than 92.75%
        Memory Usage: 13.9 MB, less than 16.42%

        1 <= nums.length <= 100
        0 <= nums[i] <= 1000
        """
        nums = sorted(nums)
        pos = 0
        for i in range(1, min(len(nums), nums[-1]) + 1):
            for j in range(pos, len(nums)):
                num = nums[j]
                if num >= i:
                    pos = j
                    break
            if len(nums) - pos == i:
                return i
        return -1


def test():
    assert Solution().specialArray([3, 5]) == 2
    assert Solution().specialArray([0, 0]) == -1


if __name__ == '__main__':
    test()
