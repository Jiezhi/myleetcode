#!/usr/bin/env python3
"""
CREATED AT: 2022-10-21

URL: https://leetcode.com/problems/node-with-highest-edge-score/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2374-NodeWithHighestEdgeScore

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        """
        Runtime: 1313 ms, faster than 89.08%
        Memory Usage: 31.8 MB, less than 44.34%
        n == edges.length
        2 <= n <= 10^5
        0 <= edges[i] < n
        edges[i] != i
        """
        ret = (0, 0)
        cnt = collections.defaultdict(int)
        for i, e in enumerate(edges):
            cnt[e] += i
            if cnt[e] > ret[1]:
                ret = (e, cnt[e])
            elif cnt[e] == ret[1]:
                ret = (min(ret[0], e), ret[1])
        return ret[0]


def test():
    assert Solution().edgeScore(edges=[1, 0, 0, 0, 0, 7, 7, 5]) == 7
    assert Solution().edgeScore(edges=[2, 0, 0, 2]) == 0
    assert Solution().edgeScore(edges=[1, 0, 0, 0, 0, 7, 7, 5]) == 7


if __name__ == '__main__':
    test()
