#!/usr/bin/env python
"""
CREATED AT: 2021/8/8
Des:
https://leetcode.com/problems/remove-stones-to-minimize-the-total
https://leetcode.com/contest/weekly-contest-253/problems/remove-stones-to-minimize-the-total/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for _ in range(k):
            piles = sorted(piles, reverse=True)
            piles[0] -= floor(piles[0] / 2)
        return sum(piles)


def test():
    assert Solution().minStoneSum(piles=[5, 4, 9], k=2) == 12
    assert Solution().minStoneSum(piles=[4, 3, 6, 7], k=3) == 12


if __name__ == '__main__':
    test()
