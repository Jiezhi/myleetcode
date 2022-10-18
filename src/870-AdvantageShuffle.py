#!/usr/bin/env python3
"""
CREATED AT: 2022-10-08

URL: https://leetcode.com/problems/advantage-shuffle/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 870-AdvantageShuffle

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        1 <= nums1.length <= 10^5
        nums2.length == nums1.length
        0 <= nums1[i], nums2[i] <= 10^9
        """
        n = len(nums1)
        nums1.sort()
        ret = [-1] * n
        n2 = sorted([(k, p) for p, k in enumerate(nums2)])
        i = 0
        for k, p in n2:
            while i < n and nums1[i] <= k:
                i += 1
            if i < n:
                ret[p] = nums1[i]
                i += 1
            else:
                break
        i = 0
        for p, v in enumerate(ret):
            if v == -1:
                ret[p] = nums1[i]
                i += 1
        return ret


def test():
    assert Solution().advantageCount(nums1=[2, 7, 11, 15], nums2=[1, 10, 4, 11]) == [2, 11, 7, 15]
    assert Solution().advantageCount(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11]) == [24, 32, 8, 12]


if __name__ == '__main__':
    test()
