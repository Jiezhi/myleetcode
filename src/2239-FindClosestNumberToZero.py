#!/usr/bin/env python
"""
CREATED AT: 2022/4/17
Des:
https://leetcode.com/problems/find-closest-number-to-zero/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        1 <= n <= 1000
        -10^5 <= nums[i] <= 10^5
        :param nums:
        :return:
        """
        ret = nums[0]
        for num in nums:
            if abs(ret) > abs(num):
                ret = num
            elif abs(ret) == abs(num):
                ret = max(ret, num)
        return ret


def test():
    assert Solution().findClosestNumber([-1, 2, 1, -4]) == 1
    assert Solution().findClosestNumber([2, -1, 1]) == 1


if __name__ == '__main__':
    test()
