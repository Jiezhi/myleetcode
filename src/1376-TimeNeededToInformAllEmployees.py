#!/usr/bin/env python
"""
CREATED AT: 2022/4/25
Des:

https://leetcode.com/problems/time-needed-to-inform-all-employees/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        Runtime: 2086 ms, faster than 33.08%
        Memory Usage: 52.9 MB, less than 21.84%

        1 <= n <= 10^5
        0 <= headID < n
        manager.length == n
        0 <= manager[i] < n
        manager[headID] == -1
        informTime.length == n
        0 <= informTime[i] <= 1000
        informTime[i] == 0 if employee i has no subordinates.
        It is guaranteed that all the employees can be informed.
        """
        adj = collections.defaultdict(list)
        for i, m in enumerate(manager):
            adj[m].append(i)

        def dfs(i) -> int:
            if i not in adj or not adj[i]:
                return 0
            return informTime[i] + max(dfs(x) for x in adj[i])

        return dfs(headID)


def test():
    assert Solution().numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]) == 1


if __name__ == '__main__':
    test()
