#!/usr/bin/env python
"""
CREATED AT: 2022/3/20
Des:
https://leetcode.com/problems/divide-array-into-equal-pairs/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 🏆 Biweekly Contest 74

See: 

"""
import collections
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        nums.length == 2 * n
        1 <= n <= 500
        1 <= nums[i] <= 500
        """
        cnt = collections.Counter(nums)
        for value in cnt.values():
            if value % 2 != 0:
                return False
        return True


def test():
    assert Solution().divideArray(nums=[3, 2, 3, 2, 2, 2])
    assert not Solution().divideArray(nums=[1, 2, 3, 4])


if __name__ == '__main__':
    test()
