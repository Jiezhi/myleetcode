#!/usr/bin/env python
"""
CREATED AT: 2021/12/20
Des:

https://leetcode.com/problems/minimum-absolute-difference/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent: 3 min
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        Runtime: 316 ms, faster than 95.83%
        Memory Usage: 28.2 MB, less than 60.76%
        2 <= arr.length <= 10^5
        -10^6 <= arr[i] <= 10^6
        :param arr:
        :return:
        """
        arr = sorted(arr)
        ret = []
        min_abs_diff = abs(arr[1] - arr[0])
        for i in range(len(arr) - 1):
            abs_diff = abs(arr[i + 1] - arr[i])
            if abs_diff == min_abs_diff:
                ret.append([arr[i], arr[i + 1]])
            elif min_abs_diff > abs_diff:
                min_abs_diff = abs_diff
                ret.clear()
                ret.append([arr[i], arr[i + 1]])
        return ret


def test():
    assert Solution().minimumAbsDifference(arr=[4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]
    assert Solution().minimumAbsDifference(arr=[1, 3, 6, 10, 15]) == [[1, 3]]
    assert Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]


if __name__ == '__main__':
    test()
