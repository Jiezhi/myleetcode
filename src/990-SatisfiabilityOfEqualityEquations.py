#!/usr/bin/env python3
"""
CREATED AT: 2022-09-26

URL: https://leetcode.com/problems/satisfiability-of-equality-equations/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 990-SatisfiabilityOfEqualityEquations

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class UnionFind:

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] == self.rank[rooty]:
            self.root[rootx] = rooty
            self.rank[rooty] += 1
        elif self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
            self.rank[rootx] = self.rank[rooty]
        else:
            self.root[rooty] = rootx
            self.rank[rooty] = rooty


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        Runtime: 107 ms, faster than 10.21%
        Memory Usage: 14.1 MB, less than 69.95%
        
        1 <= equations.length <= 500
        equations[i].length == 4
        equations[i][0] is a lowercase letter.
        equations[i][1] is either '=' or '!'.
        equations[i][2] is '='.
        equations[i][3] is a lowercase letter.
        """
        ord_a = ord('a')

        equal_uf = UnionFind(26)

        not_equal_list = []

        for exp in equations:
            a, b = ord(exp[0]) - ord_a, ord(exp[-1]) - ord_a
            if exp[1] == '!':
                not_equal_list.append((a, b))
            else:
                equal_uf.union(a, b)
        while not_equal_list:
            a, b = not_equal_list.pop()
            if equal_uf.connected(a, b):
                return False

        return True


def test():
    assert not Solution().equationsPossible(equations=["a==b", "b!=a"])
    assert not Solution().equationsPossible(equations=["a==b", "b!=c", "c==a"])
    assert Solution().equationsPossible(equations=["b==a", "a==b"])


if __name__ == '__main__':
    test()
