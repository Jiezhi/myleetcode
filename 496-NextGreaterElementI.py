#!/usr/bin/env python
"""
CREATED AT: 2021/10/19
Des:

https://leetcode.com/problems/next-greater-element-i/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 94 ms, faster than 19.85%
        Memory Usage: 14.5 MB, less than 73.08%

        1 <= nums1.length <= nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 10**4
        All integers in nums1 and nums2 are unique.
        All the integers of nums1 also appear in nums2.
        :param nums1:
        :param nums2:
        :return:
        """
        ret = []
        for num in nums1:
            index = nums2.index(num)
            for n in nums2[index + 1:]:
                if n > num:
                    ret.append(n)
                    break
            else:
                ret.append(-1)
        return ret


def test():
    assert Solution().nextGreaterElement(nums1=[4], nums2=[4]) == [-1]
    assert Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]) == [-1, 3, -1]
    assert Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]) == [3, -1]
    assert Solution().nextGreaterElement(nums1=[2, 4, 3, 1], nums2=[4, 3, 2, 1]) == [-1, -1, -1, -1]


if __name__ == '__main__':
    test()
