#!/usr/bin/env python
"""
CREATED AT: 2021/9/8
Des:
https://leetcode.com/problems/search-in-rotated-sorted-array
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        195 / 195 test cases passed.
        Status: Accepted
        Runtime: 60 ms
        Memory Usage: 14.7 MB
        :param nums:
        :param target:
        :return:
        """
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + (h - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                # ordered
                if nums[l] <= nums[mid]:
                    if nums[l] > target:
                        # might be in nums[mid + 1, h]
                        l = mid + 1
                    else:
                        # might be in nums[l, mid - 1]
                        h = mid - 1
                else:
                    # not ordered
                    h = mid - 1
            else:
                if nums[l] > nums[mid]:
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        h = mid - 1
                else:
                    l = mid + 1

        return -1


def test():
    assert Solution().search(nums=[1, 3], target=3) == 1
    assert Solution().search(nums=[1, 3], target=1) == 0
    assert Solution().search(nums=[3, 1], target=1) == 1
    assert Solution().search(nums=[3, 1], target=3) == 0
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=4) == 0
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert Solution().search(nums=[1], target=0) == -1
    assert Solution().search(nums=[1], target=1) == 0


if __name__ == '__main__':
    test()
