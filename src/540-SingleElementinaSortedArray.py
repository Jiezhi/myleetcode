#!/usr/bin/env python
"""
CREATED AT: 2021/11/20
Des:

https://leetcode.com/problems/single-element-in-a-sorted-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: BinarySearch

See: 
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Runtime: 117 ms, faster than 10.42%
        Memory Usage: 16.3 MB, less than 94.67%
        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^5
        :param nums:
        :return:
        """
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if (nums[mid] == nums[mid - 1] and mid % 2 == 1) or (nums[mid] == nums[mid + 1] and mid % 2 == 0):
                l = mid + 1
            else:
                h = mid - 1
        return nums[l]


def test():
    assert Solution().singleNonDuplicate(nums=[1]) == 1
    assert Solution().singleNonDuplicate(nums=[1, 1, 2, 2, 3]) == 3
    assert Solution().singleNonDuplicate(nums=[1, 1, 2, 2, 4, 4, 5, 5, 9]) == 9
    assert Solution().singleNonDuplicate(nums=[2, 2, 3]) == 3
    assert Solution().singleNonDuplicate(nums=[1, 2, 2]) == 1
    assert Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert Solution().singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]) == 10


if __name__ == '__main__':
    test()
