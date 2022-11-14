#!/usr/bin/env python3
"""
CREATED AT: 2022-11-14

URL: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 947-MostStonesRemovedWithSameRowOrColumn

Difficulty: 

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Runtime: 221 ms, faster than 84.98%
        Memory Usage: 14.9 MB, less than 43.51%
        1 <= stones.length <= 1000
        0 <= xi, yi <= 10^4
        No two stones are at the same coordinate point.
        """
        xd, yd = collections.defaultdict(set), collections.defaultdict(set)
        for x, y in stones:
            xd[x].add(y)
            yd[y].add(x)
        ret = 0
        for x, y in stones:
            if y in xd[x]:
                ret += 1
                stack = [(x, y)]
                while stack:
                    a, b = stack.pop()
                    stack += [(x, b) for x in yd[b]]
                    stack += [(a, x) for x in xd[a]]
                    del yd[b]
                    del xd[a]
        return len(stones) - ret


def test():
    assert Solution().removeStones(stones=[[0, 1], [1, 0]]) == 0
    assert Solution().removeStones(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
    assert Solution().removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
    assert Solution().removeStones(stones=[[0, 0]]) == 0


if __name__ == '__main__':
    test()
