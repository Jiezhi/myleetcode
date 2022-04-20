#!/usr/bin/env python
"""
CREATED AT: 2022/4/20
Des:

https://leetcode.com/problems/combinations/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Runtime: 106 ms, faster than 90.91%
        Memory Usage: 15.9 MB, less than 85.63%

        1 <= n <= 20
        1 <= k <= n
        """
        ret = []

        def comb(pos, lst):
            if len(lst) == k:
                ret.append(lst)
                return
            if len(lst) + n - pos + 1 < k:
                return

            for i in range(pos, n + 1):
                comb(i + 1, lst + [i])

        comb(1, [])
        return ret


def test():
    assert Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


if __name__ == '__main__':
    test()
