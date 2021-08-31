#!/usr/bin/env python
"""
CREATED AT: 2021/8/31
Des:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/617/week-5-august-29th-august-31st/3958/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        150 / 150 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 14.7 MB
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        mid = (len(nums) - 1) // 2
        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            return nums[mid]
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] >= nums[-1]:
            return self.findMin(nums[mid + 1:])
        else:
            return self.findMin(nums[:mid])


def test():
    assert Solution().findMin(nums=[3]) == 3
    assert Solution().findMin(nums=[3, 4, 5]) == 3
    assert Solution().findMin(nums=[3, 4, 5, 0]) == 0
    assert Solution().findMin(nums=[6, 3, 4, 5]) == 3
    assert Solution().findMin(nums=[6, 7, 3, 4, 5]) == 3
    assert Solution().findMin(nums=[3, 4, 5, 1, 2]) == 1
    assert Solution().findMin(nums=[4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin(nums=[11, 13, 15, 17]) == 11


if __name__ == '__main__':
    test()
