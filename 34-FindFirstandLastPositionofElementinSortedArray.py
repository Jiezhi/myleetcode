#!/usr/bin/env python
"""
CREATED AT: 2021/9/8
Des:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        88 / 88 test cases passed.
        Status: Accepted
        Runtime: 88 ms
        Memory Usage: 15.3 MB
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        l, h = 0, len(nums) - 1
        found = False
        while l <= h:
            mid = l + (h - l) // 2
            if target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                found = True
                break

        if not found:
            return [-1, -1]
        bh = mid - 1
        while l < bh:
            bmid = l + (bh - l) // 2
            if nums[bmid] < target:
                l = bmid + 1
            else:
                bh = bmid - 1
        al = mid + 1
        while al < h:
            bmid = al + (h - al) // 2
            if nums[bmid] <= target:
                al = bmid + 1
            else:
                h = bmid - 1
        return [l if nums[l] == target else l + 1, h if nums[h] == target else h - 1]


def test():
    assert Solution().searchRange(nums=[1], target=1) == [0, 0]
    assert Solution().searchRange(nums=[5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 10], target=7) == [1, 12]
    assert Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert Solution().searchRange(nums=[5, 7, 7, 8, 9, 10], target=8) == [3, 3]
    assert Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert Solution().searchRange(nums=[], target=0) == [-1, -1]


if __name__ == '__main__':
    test()
