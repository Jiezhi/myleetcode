#!/usr/bin/env python
"""
CREATED AT: 2021/9/5
Des:
https://leetcode.com/problems/count-special-quadruplets
https://leetcode.com/contest/weekly-contest-257/problems/count-special-quadruplets/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ret += 1
        return ret


def test():
    assert Solution().countQuadruplets([9, 6, 8, 23, 39, 23]) == 2
    assert Solution().countQuadruplets(nums=[1, 2, 3, 6]) == 1
    assert Solution().countQuadruplets(nums=[1, 1, 1, 3, 5]) == 4
    assert Solution().countQuadruplets(nums=[3, 3, 6, 4, 5]) == 0


if __name__ == '__main__':
    test()
