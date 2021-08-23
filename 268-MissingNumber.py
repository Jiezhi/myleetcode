#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/missing-number/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/722/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        122 / 122 test cases passed.
        Status: Accepted
        Runtime: 128 ms
        Memory Usage: 15.2 MB
        :param nums:
        :return:
        """
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)


def test():
    assert Solution().missingNumber(nums=[3, 0, 1]) == 2
    assert Solution().missingNumber(nums=[0, 1]) == 2
    assert Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert Solution().missingNumber(nums=[0]) == 1


if __name__ == '__main__':
    test()
