#!/usr/bin/env python
"""
CREATED AT: 2022/4/12
Des:
https://leetcode.com/problems/kth-missing-positive-number/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: https://leetcode.com/problems/kth-missing-positive-number/discuss/779999/JavaC%2B%2BPython-O(logN)

"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Runtime: 48 ms, faster than 96.67%
        Memory Usage: 14.1 MB, less than 14.60%

        1 <= arr.length <= 1000
        1 <= arr[i] <= 1000
        1 <= k <= 1000
        arr[i] < arr[j] for 1 <= i < j <= arr.length
        """
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] - mid - 1 < k:
                lo = mid + 1
            else:
                hi = mid

        return hi + k


def test():
    assert Solution().findKthPositive(arr=[2, 3, 4, 7, 11], k=5) == 9
    assert Solution().findKthPositive(arr=[1, 2, 3, 4], k=2) == 6


if __name__ == '__main__':
    test()
