#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/3

Leetcode: https://leetcode.com/problems/max-consecutive-ones/

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ret = 0
        cur = 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                ret = max(ret, cur)
                cur = 0
        return max(ret, cur)


def test():
    assert Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3


if __name__ == '__main__':
    test()
