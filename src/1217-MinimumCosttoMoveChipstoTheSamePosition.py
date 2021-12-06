#!/usr/bin/env python
"""
CREATED AT: 2021/12/6
Des:

https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        Runtime: 28 ms, faster than 90.17%
        Memory Usage: 14.4 MB, less than 19.23%
        1 <= position.length <= 100
        1 <= position[i] <= 10^9
        :param position:
        :return:
        """
        odd, even = 0, 0
        for pos in position:
            if (pos & 1) == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)


def test():
    assert Solution().minCostToMoveChips(position=[1, 2, 3]) == 1
    assert Solution().minCostToMoveChips(position=[2, 2, 2, 3, 3]) == 2
    assert Solution().minCostToMoveChips(position=[1, 1000000000]) == 1


if __name__ == '__main__':
    test()
