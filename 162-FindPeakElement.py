#!/usr/bin/env python
"""
CREATED AT: 2021/9/7
Des:
https://leetcode.com/problems/find-peak-element
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/801/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        63 / 63 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 14.4 MB
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i


def test():
    assert Solution().findPeakElement(nums=[1, 2, 3, 1]) == 2
    assert Solution().findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]) in [1, 5]


if __name__ == '__main__':
    test()
