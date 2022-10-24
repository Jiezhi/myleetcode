#!/usr/bin/env python
"""
CREATED AT: 2021/7/23
Des:
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

GITHUB: https://github.com/Jiezhi/myleetcode

"""
from tool import *


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        2022/10/24
        Runtime: 3255 ms, faster than 18.25%
        Memory Usage: 28.1 MB, less than 23.65%

        2 <= nums.length <= 10^5
        0 <= nums[i] <= 10^6
        There is at least one valid answer for the given input.
        """
        n = len(nums)
        small = [nums[0]]
        large = [nums[-1]]
        for i in range(1, n):
            small.append(max(small[i - 1], nums[i]))
            j = n - i - 1
            large.append(min(large[i - 1], nums[j]))
        large = large[::-1]

        for i in range(n - 1):
            if small[i] <= large[i + 1]:
                return i + 1

    def partitionDisjoint2(self, nums: List[int]) -> int:
        l_max = tmp_max = nums[0]
        l_len = 1
        going_compare = False
        for i in range(1, len(nums)):
            if l_max > nums[i]:
                if going_compare:
                    # found a right value less than left
                    l_max = tmp_max
                    going_compare = False
                l_len = i + 1
            else:
                going_compare = True
                tmp_max = max(nums[i], tmp_max)
        return l_len


def test():
    assert Solution().partitionDisjoint([24, 11, 49, 80, 63, 8, 61, 22, 73, 85]) == 9
    assert Solution().partitionDisjoint([5, 0, 3, 8, 6]) == 3
    assert Solution().partitionDisjoint([1, 2]) == 1
    assert Solution().partitionDisjoint([2, 2]) == 1
    assert Solution().partitionDisjoint([5, 0, 3, 8, 4, 6, 9]) == 6
    assert Solution().partitionDisjoint([1, 1, 1, 0, 6, 12]) == 4
    assert Solution().partitionDisjoint([5, 4, 3, 2, 8]) == 4


if __name__ == '__main__':
    test()
