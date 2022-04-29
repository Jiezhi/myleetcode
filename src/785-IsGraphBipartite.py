#!/usr/bin/env python
"""
CREATED AT: 2022/4/29
Des:
https://leetcode.com/problems/is-graph-bipartite/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        80 / 80 test cases passed.
        Runtime: 418 ms, faster than 5.73%
        Memory Usage: 15 MB,
        graph.length == n
        1 <= n <= 100
        0 <= graph[u].length < n
        0 <= graph[u][i] <= n - 1
        graph[u] does not contain u.
        All the values of graph[u] are unique.
        If graph[u] contains v, then graph[v] contains u.
        """
        a, b = set(), set()
        dq = collections.deque()
        for i, adj in enumerate(graph):
            if i in a or i in b:
                continue
            a.add(i)
            for j in adj:
                dq.append((j, 'b'))

            while dq:
                node, to = dq.popleft()
                if to == 'b':
                    if node in a:
                        return False
                    b.add(node)
                    for j in graph[node]:
                        if j not in a:
                            dq.append((j, 'a'))
                else:
                    if node in b:
                        return False
                    a.add(node)
                    for j in graph[node]:
                        if j not in b:
                            dq.append((j, 'b'))
        return True


def test():
    assert not Solution().isBipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert Solution().isBipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]])


if __name__ == '__main__':
    test()
