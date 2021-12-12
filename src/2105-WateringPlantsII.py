#!/usr/bin/env python
"""
CREATED AT: 2021/12/12
Des:
https://leetcode.com/problems/watering-plants-ii
https://leetcode.com/contest/weekly-contest-271/problems/watering-plants-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 8 min
"""
from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        """
        n == plants.length
        1 <= n <= 10^5
        1 <= plants[i] <= 10^6
        max(plants[i]) <= capacityA, capacityB <= 10^9
        :param plants:
        :param capacityA:
        :param capacityB:
        :return:
        """
        if len(plants) <= 1:
            return 0
        i, j = 0, len(plants) - 1
        ca, cb = capacityA, capacityB
        ret = 0
        while i < j:
            if ca < plants[i]:
                ca = capacityA
                ret += 1
            if cb < plants[j]:
                cb = capacityB
                ret += 1
            ca -= plants[i]
            cb -= plants[j]
            i += 1
            j -= 1
        if i == j and plants[i] > max(ca, cb):
            ret += 1
        return ret


def test():
    assert Solution().minimumRefill(plants=[2, 2, 3, 3], capacityA=5, capacityB=5) == 1
    assert Solution().minimumRefill(plants=[2, 2, 3, 3], capacityA=3, capacityB=4) == 2
    assert Solution().minimumRefill(plants=[5], capacityA=10, capacityB=8) == 0
    assert Solution().minimumRefill(plants=[1, 2, 4, 4, 5], capacityA=6, capacityB=5) == 2
    assert Solution().minimumRefill(plants=[2, 2, 5, 2, 2], capacityA=5, capacityB=5) == 1


if __name__ == '__main__':
    test()
