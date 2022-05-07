#!/usr/bin/env python
"""
CREATED AT: 2022/5/7
Des:
https://leetcode.com/problems/132-pattern/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import math
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Runtime: 482 ms, faster than 44.23%
        Memory Usage: 32 MB, less than 67.82%
        n == nums.length
        1 <= n <= 2 * 10^5
        -10^9 <= nums[i] <= 10^9
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return False
        # reverse then search pattern 231
        nums.reverse()

        mono = [nums[0]]
        p2 = -math.inf
        for num in nums[1:]:
            if num < p2:
                return True
            while mono and mono[-1] < num:
                p2 = mono.pop()
            if num > p2:
                mono.append(num)
        return False


def test():
    assert Solution().find132pattern([1, 2, 3, 4]) == False
    assert Solution().find132pattern([3, 1, 4, 2]) == True


if __name__ == '__main__':
    test()
