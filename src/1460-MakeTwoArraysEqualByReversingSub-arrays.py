#!/usr/bin/env python3
"""
CREATED AT: 2022-08-24

URL: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1460-MakeTwoArraysEqualByReversingSub-arrays

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        Runtime: 96 ms, faster than 81.17% 
        Memory Usage: 14.2 MB, less than 42.20% 

        target.length == arr.length
        1 <= target.length <= 1000
        1 <= target[i] <= 1000
        1 <= arr[i] <= 1000
        """
        return Counter(target) == Counter(arr)


def test():
    assert Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3])
    assert Solution().canBeEqual(target=[7], arr=[7])
    assert not Solution().canBeEqual(target=[3, 7, 9], arr=[3, 7, 11])


if __name__ == '__main__':
    test()
