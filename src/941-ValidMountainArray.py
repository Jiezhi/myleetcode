#!/usr/bin/env python
"""
Created on 2020/11/30

Des:  https://leetcode.com/problems/valid-mountain-array/

https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

https://leetcode.com/problems/valid-mountain-array/solution/

"""
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Updated at 2022/01/25
        Runtime: 422 ms, faster than 5.11%
        Memory Usage: 15.3 MB, less than 97.67%
        1 <= arr.length <= 10^4
        0 <= arr[i] <= 10^4
        :param arr:
        :return:
        """
        if len(arr) < 3:
            return False
        if arr[1] <= arr[0]:
            return False
        flag = False
        for i in range(2, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            if not flag and arr[i] < arr[i - 1]:
                flag = True
            elif flag and arr[i] > arr[i - 1]:
                return False

        return flag

    def validMountainArray2(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        incr = True
        for i in range(len(arr) - 1):
            if incr and arr[i] < arr[i + 1]:
                continue
            # the first value larger than second value is not mountain array
            if i == 0:
                return False
            incr = False
            if arr[i] <= arr[i + 1]:
                return False
        if incr:
            return False
        else:
            return True


def test():
    assert not Solution().validMountainArray([1, 2, 3, 4])
    assert not Solution().validMountainArray([2, 1])
    assert not Solution().validMountainArray([3, 5, 5])
    assert not Solution().validMountainArray([3, 5, 5, 4])
    assert not Solution().validMountainArray([5, 4, 3])
    assert Solution().validMountainArray([0, 3, 2, 1])
    assert Solution().validMountainArray([0, 1, 2, 3, 2, 1])


if __name__ == '__main__':
    test()
