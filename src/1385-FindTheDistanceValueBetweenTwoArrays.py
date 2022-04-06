#!/usr/bin/env python
"""
CREATED AT: 2022/4/6
Des:
https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Runtime: 88 ms, faster than 91.26%
        Memory Usage: 14.1 MB, less than 9.91%

        :param arr1: 1 <= arr1.length, arr2.length <= 500
                    -1000 <= arr1[i], arr2[j] <= 1000
                    0 <= d <= 100
        :param arr2:
        :param d:
        :return:
        """
        if d == 0:
            return 0
        ret = 0
        arr2 = sorted(arr2)
        for num in arr1:
            lo, hi = 0, len(arr2) - 1
            valid = True
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr2[mid] == num or abs(num - arr2[mid]) <= d:
                    valid = False
                    break
                elif arr2[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
            ret += valid
        return ret


def test():
    pass


if __name__ == '__main__':
    test()
