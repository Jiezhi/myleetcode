#!/usr/bin/env python
"""
CREATED AT: 2021/9/7
Des:
https://leetcode.com/problems/kth-largest-element-in-an-array/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        32 / 32 test cases passed.
        Status: Accepted
        Runtime: 90 ms
        Memory Usage: 15.1 MB
        :param nums:
        :param k:
        :return:
        """
        # return sorted(nums)[-k]
        return sorted(nums, reverse=True)[k - 1]


def test():
    assert Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2) == 5
    assert Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4) == 4


if __name__ == '__main__':
    test()
