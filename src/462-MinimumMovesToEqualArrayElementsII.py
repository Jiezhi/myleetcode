#!/usr/bin/env python3
"""
CREATED AT: 2022-06-30

URL: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 462-MinimumMovesToEqualArrayElementsII

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        Runtime: 148 ms, faster than 17.14% 
        Memory Usage: 15.4 MB, less than 79.18% 

        n == nums.length
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        """
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(mid - num) for num in nums)


def test():
    assert Solution().minMoves2(nums=[1]) == 0
    assert Solution().minMoves2(nums=[1, 2]) == 1
    assert Solution().minMoves2(nums=[1, 2, 3]) == 2
    assert Solution().minMoves2(nums=[1, 10, 2, 9]) == 16


if __name__ == '__main__':
    test()
