#!/usr/bin/env python
"""
Created on 2020/11/30

Des:  https://leetcode.com/problems/check-if-n-and-its-double-exist/

https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/

"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
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


if __name__ == '__main__':
    test()
