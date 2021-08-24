#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:
https://leetcode.com/problems/binary-search/
https://leetcode.com/study-plan/algorithm/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        46 / 46 test cases passed.
        Status: Accepted
        Runtime: 240 ms
        Memory Usage: 15.5 MB
        :param nums:
        :param target:
        :return:
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


def test():
    assert Solution().search(nums=[1, 5], target=5) == 1
    assert Solution().search(nums=[5], target=5) == 0
    assert Solution().search(nums=[5, 8], target=5) == 0
    assert Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1


if __name__ == '__main__':
    test()
