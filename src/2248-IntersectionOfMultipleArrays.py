#!/usr/bin/env python
"""
CREATED AT: 2022/4/24
Des:
https://leetcode.com/problems/intersection-of-multiple-arrays/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        """
        Runtime: 74 ms, faster than 80.00%
        Memory Usage: 14.1 MB, less than 100.00%

        1 <= nums.length <= 1000
        1 <= sum(nums[i].length) <= 1000
        1 <= nums[i][j] <= 1000
        All the values of nums[i] are unique.
        """
        ret = set(nums[0])
        for num in nums[1:]:
            ret &= set(num)
            if not ret:
                return []
        return sorted(list(ret))


def test():
    assert Solution().intersection(nums=[[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]) == [3, 4]
    assert Solution().intersection(nums=[[1, 2, 3], [4, 5, 6]]) == []


if __name__ == '__main__':
    test()
