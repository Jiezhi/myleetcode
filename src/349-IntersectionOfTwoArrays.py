#!/usr/bin/env python
"""
CREATED AT: 2022/3/16
Des:

https://leetcode.com/problems/intersection-of-two-arrays/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 84 ms, faster than 28.60%
        Memory Usage: 14.2 MB, less than 45.27%
        
        1 <= nums1.length, nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 1000
        """
        return list(set(nums1) & set(nums2))


def test():
    assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]) in [[9, 4], [4, 9]]


if __name__ == '__main__':
    test()
