#!/usr/bin/env python
"""
CREATED AT: 2021/7/23
Des:
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = nums[tmp - 1]
            nums[tmp - 1] = tmp
            print(nums)
        pass


def test():
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert Solution().findDisappearedNumbers([1, 1]) == [2]


if __name__ == '__main__':
    test()
