#!/usr/bin/env python
"""
CREATED AT: 2021/9/4
Des:
https://leetcode.com/problems/find-all-groups-of-farmland
https://leetcode.com/contest/biweekly-contest-60/problems/find-all-groups-of-farmland/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        pass


def test():
    assert Solution().findFarmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [[0, 0, 0, 0], [1, 1, 2, 2]]
    assert Solution().findFarmland(land=[[1, 1], [1, 1]]) == [[0, 0, 1, 1]]
    assert Solution().findFarmland(land=[[0]]) == []


if __name__ == '__main__':
    test()
