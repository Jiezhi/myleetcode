#!/usr/bin/env python
"""
CREATED AT: 2022/3/27
Des:
https://leetcode.com/problems/find-the-difference-of-two-arrays/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1 - s2), list(s2 - s1)]


def test():
    assert Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]) == [[1, 3], [4, 6]]


if __name__ == '__main__':
    test()
