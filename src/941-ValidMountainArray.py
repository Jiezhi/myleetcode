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
    assert not Solution().validMountainArray([2, 1])
    assert not Solution().validMountainArray([3, 5, 5])
    assert not Solution().validMountainArray([3, 5, 5, 4])
    assert not Solution().validMountainArray([5, 4, 3])
    assert Solution().validMountainArray([0, 3, 2, 1])
    assert Solution().validMountainArray([0, 1, 2, 3, 2, 1])


if __name__ == '__main__':
    test()
