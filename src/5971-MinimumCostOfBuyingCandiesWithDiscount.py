#!/usr/bin/env python
"""
CREATED AT: 2022/1/22
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        CREATED AT: 2022/1/22
        1 <= cost.length <= 100
        1 <= cost[i] <= 100
        :param cost:
        :return:
        """
        ret = 0
        cost = sorted(cost, reverse=True)
        i = 1
        while i <= len(cost):
            if i % 3 != 0:
                ret += cost[i - 1]
            i += 1
        return ret


def test():
    assert Solution().minimumCost(cost=[1, 2, 3]) == 5
    assert Solution().minimumCost(cost=[6, 5, 7, 9, 2, 2]) == 23
    assert Solution().minimumCost(cost=[5, 5]) == 10


if __name__ == '__main__':
    test()
