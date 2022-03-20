#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:

https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: Weekly Contest 285

See: 

"""
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ret = 0
        l = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                l.append(nums[i])

        for i in range(1, len(l) - 1):
            if l[i - 1] < l[i] > l[i + 1] or l[i - 1] > l[i] < l[i + 1]:
                ret += 1
        return ret


def test():
    assert Solution().countHillValley(nums=[2, 4, 1, 1, 6, 5]) == 3
    assert Solution().countHillValley(nums=[6, 6, 5, 5, 4, 1]) == 0


if __name__ == '__main__':
    test()
