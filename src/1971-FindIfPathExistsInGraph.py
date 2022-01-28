#!/usr/bin/env python
"""
CREATED AT: 2022/1/28
Des:

https://leetcode.com/problems/find-if-path-exists-in-graph/
https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3893/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            else:
                self.root[ry] = rx
                self.rank[rx] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        CREATED AT: 2022/1/28
        25 / 25 test cases passed.
        Status: Accepted
        Runtime: 3405 ms, faster than 15.86%
        Memory Usage: 103.6 MB, less than 99.46%

        After add the code:
        >>> if uf.connected(source, destination):
        >>>    return True
        25 / 25 test cases passed.
        Status: Accepted
        Runtime: 1828 ms, faster than 77.33%
        Memory Usage: 103.9 MB, less than 98.25%

        1 <= n <= 2 * 10^5
        0 <= edges.length <= 2 * 10^5
        edges[i].length == 2
        0 <= ui, vi <= n - 1
        ui != vi
        0 <= source, destination <= n - 1
        There are no duplicate edges.
        There are no self edges.
        :param n:
        :param edges:
        :param source:
        :param destination:
        :return:
        """
        if source == destination:
            return True

        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
            if uf.connected(source, destination):
                return True
        return uf.connected(source, destination)

    def validPath2(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        CREATED AT: 2022/1/28
        25 / 25 test cases passed.
        Status: Accepted
        Runtime: 4011 ms, faster than 5.3%
        Memory Usage: 324.7 MB, less than 20.95%
        1 <= n <= 2 * 10^5
        0 <= edges.length <= 2 * 10^5
        edges[i].length == 2
        0 <= ui, vi <= n - 1
        ui != vi
        0 <= source, destination <= n - 1
        There are no duplicate edges.
        There are no self edges.
        :param n:
        :param edges:
        :param source:
        :param destination:
        :return:
        """
        if source == destination:
            return True

        edge_dict = defaultdict(list)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])

        visited = set()

        def dfs(src, dest, edge_dict) -> bool:
            if (src, dest) in visited:
                return False
            visited.add((src, dest))

            for value in edge_dict[src]:
                if value == dest:
                    return True
                if dfs(value, dest, edge_dict):
                    return True
            return False

        if source not in edge_dict or destination not in edge_dict:
            return False

        return dfs(source, destination, edge_dict)


def test():
    assert Solution().validPath(
        n=10,
        edges=[[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
        source=5, destination=9)
    assert Solution().validPath(n=1, edges=[], source=0, destination=0)
    assert Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert not Solution().validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5)


if __name__ == '__main__':
    test()
