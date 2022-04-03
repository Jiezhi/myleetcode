#!/usr/bin/env python
"""
CREATED AT: 2022/4/3
Des:
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        candies = sorted(candies, reverse=True)

        def canDivide(cnt: int) -> bool:
            ret = 0
            for c in candies:
                ret += c // cnt
                if ret >= k:
                    return True
            return False

        if total < k:
            return 0
        lo, hi = 1, total // k
        while lo < hi - 1:
            mid = lo + (hi - lo) // 2
            if canDivide(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo + 1 if canDivide(lo + 1) else lo


def test():
    assert Solution().maximumCandies(candies=[5, 8, 6], k=3) == 5


if __name__ == '__main__':
    test()
