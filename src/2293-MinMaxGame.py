#!/usr/bin/env python3
"""
CREATED AT: 2023-01-15

URL: https://leetcode.com/problems/min-max-game/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2293-MinMaxGame

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.minMaxGame(
            [max(nums[i], nums[i + 1]) if (i // 2) & 1 else min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)])


def test():
    assert Solution().minMaxGame(nums=[1, 3, 5, 2, 4, 8, 2, 2]) == 1
    assert Solution().minMaxGame(nums=[3]) == 3


if __name__ == '__main__':
    test()
