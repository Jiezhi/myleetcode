#!/usr/bin/env python
"""
CREATED AT: 2021/7/23
Des:
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
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
