#!/usr/bin/env python
"""
Created on 2020/11/30

Des:  https://leetcode.com/problems/check-if-n-and-its-double-exist/

https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Runtime: 85 ms, faster than 42.78%
        Memory Usage: 14 MB, less than 17.67%

        2 <= arr.length <= 500
        -10^3 <= arr[i] <= 10^3
        """
        arr = sorted(arr)

        def bs(lo, hi, target) -> bool:
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False

        for i, num in enumerate(arr):
            if num < 0 and num % 2 == 0:
                if bs(i + 1, len(arr) - 1, num // 2):
                    return True
            elif num == 0 and i < len(arr) - 1 and arr[i + 1] == 0:
                return True
            elif num > 0:
                if bs(i + 1, len(arr) - 1, num * 2):
                    return True
        return False

    def checkIfExist2(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] == arr[i] * 2 and j != i:
                    return True
        return False


def test():
    assert Solution().checkIfExist([10, 2, 5, 3])
    assert Solution().checkIfExist([7, 1, 14, 11])
    assert not Solution().checkIfExist([3, 1, 7, 11])
    assert not Solution().checkIfExist([-2, 0, 10, -19, 4, 6, -8])
    assert Solution().checkIfExist([-10, 12, -20, -8, 15])


if __name__ == '__main__':
    test()
