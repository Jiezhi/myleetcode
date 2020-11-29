#!/usr/bin/env python
"""
Created on 2020/11/29

Des:  https://leetcode.com/problems/squares-of-a-sorted-array/

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x * x for x in A])


def test():
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


if __name__ == '__main__':
    test()
