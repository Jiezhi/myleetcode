#!/usr/bin/env python
"""
CREATED AT: 2022/1/9
Des:

https://leetcode.com/contest/weekly-contest-275/problems/minimum-swaps-to-group-all-1s-together-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        1 <= nums.length <= 10^5
        nums[i] is either 0 or 1.
        :param nums:
        :return:
        """
        n_one = sum(nums)
        ret = len(nums)
        num_bit = ''.join(str(x) for x in nums)
        num = int(num_bit, 2)
        tmp_num = 2 ** n_one - 1
        for i in range(len(nums) - n_one):
            tmp_num <<= 1
            pass
        pass


def test():
    assert Solution().minSwaps(nums=[0, 1, 0, 1, 1, 0, 0]) == 1
    assert Solution().minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2
    assert Solution().minSwaps(nums=[1, 1, 0, 0, 1]) == 0


if __name__ == '__main__':
    test()
