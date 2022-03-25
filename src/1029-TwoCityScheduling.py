#!/usr/bin/env python
"""
CREATED AT: 2022/3/25
Des:

https://leetcode.com/problems/two-city-scheduling/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""
from functools import lru_cache
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Runtime: 85 ms, faster than 12.68%
        Memory Usage: 15.7 MB, less than 5.07%
        
        2 * n == costs.length
        2 <= costs.length <= 100
        costs.length is even.
        1 <= aCosti, bCosti <= 1000
        """
        n = len(costs) // 2

        @lru_cache(None)
        def dp(la, lb, pos):
            if pos >= 2 * n:
                return 0
            if la >= n:
                return costs[pos][1] + dp(la, lb + 1, pos + 1)
            if lb >= n:
                return costs[pos][0] + dp(la + 1, lb, pos + 1)

            return min(costs[pos][1] + dp(la, lb + 1, pos + 1), costs[pos][0] + dp(la + 1, lb, pos + 1))

        return dp(0, 0, 0)


def test():
    assert Solution().twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
    assert Solution().twoCitySchedCost(
        costs=[[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
    assert Solution().twoCitySchedCost(
        costs=[[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086


if __name__ == '__main__':
    test()
