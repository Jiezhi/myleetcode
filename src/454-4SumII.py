#!/usr/bin/env python
"""
CREATED AT: 2022/1/4
Des:

https://leetcode.com/problems/4sum-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        Ref: https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
        132 / 132 test cases passed.
        Status: Accepted
        Runtime: 829 ms
        Memory Usage: 14.2 MB
        n == nums1.length
        n == nums2.length
        n == nums3.length
        n == nums4.length
        1 <= n <= 200
        -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
        :param nums1:
        :param nums2:
        :param nums3:
        :param nums4:
        :return:
        """
        sum_of_two_count = collections.Counter(num1 + num2 for num1 in nums1 for num2 in nums2)
        return sum(sum_of_two_count[-(num3 + num4)] for num3 in nums3 for num4 in nums4)


def test():
    assert Solution().fourSumCount(nums1=[0] * 200, nums2=[0] * 200, nums3=[0] * 200, nums4=[0] * 200) == 200 ** 4
    assert Solution().fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]) == 2
    assert Solution().fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]) == 1


if __name__ == '__main__':
    test()
