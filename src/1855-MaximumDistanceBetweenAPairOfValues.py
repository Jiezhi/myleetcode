#!/usr/bin/env python
"""
CREATED AT: 2022/4/12
Des:
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Runtime: 1977 ms, faster than 27.56%
        Memory Usage: 32.5 MB, less than 57.69%

        1 <= nums1.length, nums2.length <= 10^5
        1 <= nums1[i], nums2[j] <= 10^5
        Both nums1 and nums2 are non-increasing.
        """
        ret = 0
        for i, num1 in enumerate(nums1):
            if i >= len(nums2):
                break
            if nums2[i] < num1 or len(nums2) - i <= ret:
                continue
            if nums2[-1] >= num1:
                ret = max(ret, len(nums2) - i - 1)
                continue

            lo, hi = i, len(nums2) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums2[mid] < num1:
                    hi = mid
                else:
                    lo = mid + 1
            ret = max(ret, hi - i - 1)
        return ret


def test():
    assert Solution().maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]) == 2
    assert Solution().maxDistance(nums1=[2, 2, 2], nums2=[10, 10, 1]) == 1
    assert Solution().maxDistance(nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]) == 2


if __name__ == '__main__':
    test()
