#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:
https://leetcode.com/contest/weekly-contest-256/problems/minimum-difference-between-highest-and-lowest-of-k-scores
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums = sorted(nums)
        ret = 10 ** 5 + 1
        for i in range(len(nums) - k + 1):
            ret = min(ret, nums[i + k - 1] - nums[i])
        return ret


def test():
    assert Solution().minimumDifference(nums=[90], k=1) == 0
    assert Solution().minimumDifference(nums=[9, 4, 1, 7], k=2) == 2


if __name__ == '__main__':
    test()
