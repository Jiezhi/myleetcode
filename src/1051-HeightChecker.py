#!/usr/bin/env python
"""
CREATED AT: 2021/7/23
Des:

https://leetcode.com/problems/height-checker/
https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3228/


GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        v = 0
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                v += 1
        return v


def test():
    assert Solution().heightChecker([1, 1, 4, 2, 1, 3]) == 3
    assert Solution().heightChecker([5, 1, 2, 3, 4]) == 5


if __name__ == '__main__':
    test()
