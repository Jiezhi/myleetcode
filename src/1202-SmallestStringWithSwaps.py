#!/usr/bin/env python
"""
CREATED AT: 2022/1/28
Des:

https://leetcode.com/problems/smallest-string-with-swaps/
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3913/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        CREATED AT: 2022/1/28
        36 / 36 test cases passed.
        Status: Accepted
        Runtime: 1949 ms
        Memory Usage: 50.4 MB, less than 99.5%
        1 <= s.length <= 10^5
        0 <= pairs.length <= 10^5
        0 <= pairs[i][0], pairs[i][1] < s.length
        s only contains lower case English letters.
        :param s:
        :param pairs:
        :return:
        """
        uf = UnionFind(len(s))
        for pair in pairs:
            uf.union(pair[0], pair[1])
        group_dict = defaultdict(dict)
        for i in range(len(s)):
            root = uf.find(i)
            d = group_dict[root]
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        ret = []
        for i in range(len(s)):
            root = uf.find(i)
            d = group_dict[root]
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) in d and d[chr(c)] > 0:
                    ret.append(chr(c))
                    d[chr(c)] -= 1
                    break
        return ''.join(ret)


def test():
    assert Solution().smallestStringWithSwaps(
        s="otilzqqoj",
        pairs=[[2, 3], [7, 3], [3, 8], [1, 7], [1, 0], [0, 4], [0, 6], [3, 4], [2, 5]]) == "ijlooqqtz"
    assert Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]) == "bacd"
    assert Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]) == "abcd"
    assert Solution().smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]) == "abc"


if __name__ == '__main__':
    test()
