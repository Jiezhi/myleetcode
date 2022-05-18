#!/usr/bin/env python
"""
CREATED AT: 2022/5/18
Des:
https://leetcode.com/problems/critical-connections-in-a-network/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
import collections
from math import inf
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        AC: 05/18/2022
        Ref: https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution
        17 / 17 test cases passed.
        Runtime: 3847 ms, faster than 19.98%
        Memory Usage: 86.4 MB, less than 29.1%
        2 <= n <= 10^5
        n - 1 <= connections.length <= 10^5
        0 <= ai, bi <= n - 1
        ai != bi
        There are no repeated connections.
        :param n:
        :param connections:
        :return:
        """
        adj = collections.defaultdict(list)
        ret = set()
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
            ret.add((u, v))

        rank = [-inf for _ in range(n)]

        def dfs(pos, depth) -> int:
            if rank[pos] >= 0:
                return rank[pos]
            rank[pos] = depth
            min_ret = n
            for neighbor in adj[pos]:
                # node[pos] is from node[neighbor] at the upper dfs
                if rank[neighbor] == rank[pos] - 1:
                    continue
                neighbor_depth = dfs(neighbor, depth + 1)
                if neighbor_depth <= depth:
                    ret.discard((pos, neighbor))
                    ret.discard((neighbor, pos))
                min_ret = min(min_ret, neighbor_depth)
            return min_ret

        dfs(0, 0)

        return [list(x) for x in ret]


def test():
    assert Solution().criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]) == [[1, 3]]


if __name__ == '__main__':
    test()
