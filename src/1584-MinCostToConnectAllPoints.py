#!/usr/bin/env python
"""
CREATED AT: 2022/1/29
Des:

https://leetcode.com/problems/min-cost-to-connect-all-points/
https://leetcode.com/explore/learn/card/graph/621/algorithms-to-construct-minimum-spanning-tree/3857/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import heapq
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
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            elif self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        CREATED AT: 2022/1/29
        72 / 72 test cases passed.
        Status: Accepted
        Runtime: 6954 ms, faster than 7.26%
        Memory Usage: 204.2 MB, less than
        1 <= points.length <= 1000
        -10^6 <= xi, yi <= 10^6
        All pairs (xi, yi) are distinct.
        :param points:
        :return:
        """
        # Prim’s Algorithm
        n = len(points)
        vertices = [(0, (0, 0))]
        heapq.heapify(vertices)
        visited = set()
        ret = 0
        while len(visited) < n:
            d, (i, _) = heapq.heappop(vertices)
            if i in visited:
                continue
            visited.add(i)
            ret += d
            for j in range(n):
                if i != j:
                    heapq.heappush(
                        vertices,
                        (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), (j, i))
                    )
        return ret

    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        """
        CREATED AT: 2022/1/29
        Runtime: 1268 ms, faster than 86.69%
        Memory Usage: 92.1 MB, less than 61.87%
        1 <= points.length <= 1000
        -10^6 <= xi, yi <= 10^6
        All pairs (xi, yi) are distinct.
        :param points:
        :return:
        """
        # Kruskal’s Algorithm
        n = len(points)
        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                edges.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        edges = sorted(edges, key=lambda x: x[2])
        connected_edges = 0
        cost = 0
        uf = UnionFind(n)
        for edge in edges:
            if not uf.connected(edge[0], edge[1]):
                uf.union(edge[0], edge[1])
                connected_edges += 1
                cost += edge[2]
                if connected_edges == n - 1:
                    break
        return cost


def test():
    assert Solution().minCostConnectPoints(points=[[-1000000, -1000000], [1000000, 1000000]]) == 4000000
    assert Solution().minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert Solution().minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]) == 18


if __name__ == '__main__':
    test()
