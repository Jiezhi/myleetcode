#!/usr/bin/env python
"""
CREATED AT: 2022/4/27
Des:
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Runtime: 1393 ms, faster than 65.14%
        Memory Usage: 52.3 MB, less than 78.33%

        2 <= n <= 10^5
        1 <= edges.length <= min(10^5, n * (n - 1) / 2)
        edges[i].length == 2
        0 <= fromi, toi < n
        All pairs (fromi, toi) are distinct.
        """
        adj = collections.defaultdict(bool)
        for f, t in edges:
            adj[t] = True
        return [i for i in range(n) if not adj[i]]


def test():
    assert Solution().findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]


if __name__ == '__main__':
    test()
