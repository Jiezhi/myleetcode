#!/usr/bin/env python
"""
CREATED AT: 2022/1/23
Des:

https://leetcode.com/contest/weekly-contest-277/problems/count-elements-with-strictly-smaller-and-greater-elements/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 100
        -10^5 <= nums[i] <= 10^5
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return 0
        nums = sorted(nums)
        i, j = 1, len(nums) - 2
        while i <= j:
            if nums[i] == nums[i - 1]:
                i += 1
            elif nums[j] == nums[j + 1]:
                j -= 1
            else:
                break

        return j - i + 1


def test():
    assert Solution().countElements(nums=[2]) == 0
    assert Solution().countElements(nums=[2, 3, 4]) == 1
    assert Solution().countElements(nums=[2, 3, 3]) == 0
    assert Solution().countElements(nums=[2, 2, 2]) == 0
    assert Solution().countElements(nums=[11, 7, 2, 15]) == 2
    assert Solution().countElements(nums=[-3, 3, 3, 90]) == 2


if __name__ == '__main__':
    test()
