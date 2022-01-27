#!/usr/bin/env python
"""
CREATED AT: 2022/1/27
Des:

https://leetcode.com/problems/number-of-provinces/
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3845/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: UnionFind

See: https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3843/

Time Spent:  min
"""
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


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        CREATED AT: 2022/1/27
        113 / 113 test cases passed.
        Status: Accepted
        Runtime: 418 ms, faster than 9.62%
        Memory Usage: 14.2 MB, less than 99.95%
        1 <= n <= 200
        n == isConnected.length
        n == isConnected[i].length
        isConnected[i][j] is 1 or 0.
        isConnected[i][i] == 1
        isConnected[i][j] == isConnected[j][i]
        :param isConnected:
        :return:
        """
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        ret = 0
        for i in range(n):
            if uf.find(i) == i:
                ret += 1
        return ret


def test():
    assert Solution().findCircleNum(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert Solution().findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


if __name__ == '__main__':
    test()
