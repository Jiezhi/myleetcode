#!/usr/bin/env python3
"""
CREATED AT: 2022-06-11

URL:https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1658-MinimumOperationsToReduceXToZero

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Runtime: 1142 ms, faster than 97.88%
        Memory Usage: 28 MB, less than 62.03%
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4
        1 <= x <= 10^9
        """
        n, ret = len(nums), -1
        remains = sum(nums) - x
        if remains < 0:
            return -1
        if remains == 0:
            return n

        i, j, s = 0, 0, 0
        while i < n:
            while j < n and s < remains:
                s += nums[j]
                j += 1
            if s == remains:
                ret = max(ret, j - i)
            s -= nums[i]
            i += 1
        if ret == -1:
            return -1
        return n - ret


def test():
    assert Solution().minOperations(nums=[1, 1, 4, 2, 3], x=5) == 2


if __name__ == '__main__':
    test()
