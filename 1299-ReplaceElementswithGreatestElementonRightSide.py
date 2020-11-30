#!/usr/bin/env python
"""
Created on 2020/11/30

Des:  https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        tmp_m = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > tmp_m:
                arr[i], tmp_m = tmp_m, arr[i]
            else:
                arr[i] = tmp_m
        return arr


def test():
    assert Solution().replaceElements([10]) == [-1]
    assert Solution().replaceElements([2, 10]) == [10, -1]
    assert Solution().replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]


if __name__ == '__main__':
    test()
