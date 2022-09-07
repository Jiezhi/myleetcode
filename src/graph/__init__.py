#!/usr/bin/env python
"""
Created on 2022/1/26

Author: 

Des:

Ref: https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3878/
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3843/

"""


class UnionFind:
    def __init__(self, size):
        self.root = [x for x in range(size)]

    def find(self, pos):
        if pos < len(self.root):
            return self.root[pos]
        else:
            raise IndexError(f'pos of {pos} is out of range {len(self.root)}')

    def connected(self, pos1, pos2):
        if pos1 >= len(self.root) or pos2 >= len(self.root):
            raise IndexError(f'pos of {pos1} or {pos2} is out of range {len(self.root)}')
        return self.root[pos1] == self.root[pos2]

    def union(self, pos1, pos2):
        if self.connected(pos1, pos2):
            return

        root1 = self.find(pos1)
        root2 = self.find(pos2)
        for i in range(len(self.root)):
            if self.root[i] == root2:
                self.root[i] = root1


class UnionFindByRank:
    def __init__(self, size):
        self.root = [x for x in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, x):
        if x < len(self.root):
            while x != self.root[x]:
                x = self.root[x]
            return x
        else:
            raise IndexError(f'pos of {x} is out of range {len(self.root)}')

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        if self.rank[rootx] < self.rank[rooty]:
            self.root[rootx] = rooty
        elif self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1


if __name__ == '__main__':
    uf = UnionFindByRank(10)
    uf.union(1, 5)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    assert uf.connected(1, 5)
    assert uf.connected(5, 7)
    assert not uf.connected(4, 9)
    uf.union(9, 4)
    assert uf.connected(4, 9)
