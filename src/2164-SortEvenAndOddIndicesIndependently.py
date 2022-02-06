#!/usr/bin/env python
"""
CREATED AT: 2022/2/6
Des:

https://leetcode.com/problems/sort-even-and-odd-indices-independently/
https://leetcode.com/contest/weekly-contest-279/problems/sort-even-and-odd-indices-independently/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        """
        Runtime: 63 ms, faster than 75.00%
        Memory Usage: 13.8 MB, less than 100.00%
        1 <= nums.length <= 100
        1 <= nums[i] <= 100
        :param nums:
        :return:
        """
        odd_list = sorted((nums[x] for x in range(1, len(nums), 2)), reverse=True)
        even_list = sorted(nums[x] for x in range(0, len(nums), 2))
        for i in range(len(even_list)):
            nums[i * 2] = even_list[i]
        for i in range(len(odd_list)):
            nums[i * 2 + 1] = odd_list[i]
        return nums


def test():
    assert Solution().sortEvenOdd(nums=[4, 1, 2, 3]) == [2, 3, 4, 1]
    assert Solution().sortEvenOdd(nums=[2, 1]) == [2, 1]
    assert Solution().sortEvenOdd(nums=[2, 1, 3]) == [2, 1, 3]
    assert Solution().sortEvenOdd(nums=[1]) == [1]


if __name__ == '__main__':
    test()
