#!/usr/bin/env python3
"""
CREATED AT: 2022-09-07

URL: https://leetcode.com/problems/number-of-operations-to-make-network-connected/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1319-NumberOfOperationsToMakeNetworkConnected

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from graph import *
from tool import *


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Runtime: 685 ms, faster than 67.35%
        Memory Usage: 34.4 MB, less than 62.25%

        1 <= n <= 10^5
        1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
        connections[i].length == 2
        0 <= ai, bi < n
        ai != bi
        There are no repeated connections.
        No two computers are connected by more than one cable.
        """
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)

        for a, b in connections:
            uf.union(a, b)
        return len(set(uf.find(x) for x in range(n))) - 1


def test():
    assert Solution().makeConnected(n=5, connections=[[0, 1], [0, 2], [3, 4], [2, 3]]) == 0
    assert Solution().makeConnected(n=4, connections=[[0, 1], [0, 2], [1, 2]]) == 1
    assert Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2
    assert Solution().makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2]]) == -1


if __name__ == '__main__':
    test()
