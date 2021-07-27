#!/usr/bin/env python
"""
CREATED AT: 2021/7/26
Des:
https://leetcode.com/problems/intersection-of-two-arrays-ii/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        55 / 55 test cases passed.
        Status: Accepted
        Runtime: 2056 ms
        Memory Usage: 14.4 MB
        :param nums1:
        :param nums2:
        :return:
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            long_nums = nums1
            short_nums = nums2
        else:
            long_nums = nums2
            short_nums = nums1
        used_nums_index = []
        intersect_nums = []
        for n in short_nums:
            for i in range(len(long_nums)):
                if i not in used_nums_index and n == long_nums[i]:
                    used_nums_index.append(i)
                    intersect_nums.append(n)
                    break
        return intersect_nums
    # * What if the given array is already sorted? How would you optimize your algorithm?
    # * What if nums1's size is small compared to nums2's size? Which algorithm is better?
    # * What if elements of nums2 are stored on disk,
    # and the memory is limited such that you cannot load all elements into the memory at once?


def test():
    assert Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2, 2]
    assert Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) in [[4, 9], [9, 4]]


if __name__ == '__main__':
    test()
