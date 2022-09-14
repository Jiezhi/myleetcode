#!/usr/bin/env python3
"""
CREATED AT: 2022-09-14

URL: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1619-MeanOfArrayAfterRemovingSomeElements

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        """
        Runtime: 56 ms, faster than 98.16%
        Memory Usage: 13.9 MB, less than 76.63%

        20 <= arr.length <= 1000
        arr.length is a multiple of 20.
        0 <= arr[i] <= 10^5
        """
        arr.sort()
        n = len(arr)
        per5 = int(n * 0.05)
        return sum(arr[per5:-per5]) / (n - 2 * per5)


def test():
    assert Solution().trimMean(arr=[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]) == 2.000
    assert Solution().trimMean(arr=[6, 2, 7, 5, 1, 2, 0, 3, 10, 2, 5, 0, 5, 5, 0, 8, 7, 6, 8, 0]) == 4.000


if __name__ == '__main__':
    test()
