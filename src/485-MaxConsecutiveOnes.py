#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/3

Leetcode: https://leetcode.com/problems/max-consecutive-ones/
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3982/

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        42 / 42 test cases passed.
        Status: Accepted
        Runtime: 340 ms
        Memory Usage: 14.1 MB
        :param nums:
        :return:
        """
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
