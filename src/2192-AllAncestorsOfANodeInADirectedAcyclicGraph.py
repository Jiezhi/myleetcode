#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from functools import lru_cache
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        1 <= n <= 1000
        0 <= edges.length <= min(2000, n * (n - 1) / 2)
        edges[i].length == 2
        0 <= fromi, toi <= n - 1
        fromi != toi
        There are no duplicate edges.
        The graph is directed and acyclic.
        """
        edge_rel = collections.defaultdict(list)
        for from_edge, to_edge in edges:
            edge_rel[to_edge].append(from_edge)

        rets = [set() for _ in range(n)]

        @lru_cache(None)
        def get_ancestor(edge: int) -> set:
            if not edge_rel[edge]:
                return None
            ret = set()
            for ancestor in edge_rel[edge]:
                ret.add(ancestor)
                ancestor_ret = get_ancestor(ancestor)
                if ancestor_ret:
                    ret = ret.union(ancestor_ret)
            return ret

        for i in range(n):
            if not edge_rel[i]:
                continue
            rets[i] = get_ancestor(i)

        return [sorted(list(x)) for x in rets]


def test():
    assert Solution().getAncestors(
        n=8,
        edges=[[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7],
               [4, 6]]) == [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4],
                            [0, 1, 2, 3]]


if __name__ == '__main__':
    test()
