#!/usr/bin/env python
"""
CREATED AT: 2022/3/17
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        Runtime: 76 ms, faster than 92.51%
        Memory Usage: 15.2 MB, less than 94.01%

        3 <= arr.length <= 10^4
        0 <= arr[i] <= 10^6
        arr is guaranteed to be a mountain array.
        """
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                lo = mid
            else:
                hi = mid


def test():
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 5


if __name__ == '__main__':
    test()
