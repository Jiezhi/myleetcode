#!/usr/bin/env python
"""
CREATED AT: 2022/4/22
Des:

https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
import collections
import heapq
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        """
        Runtime: 3270 ms, faster than 13.19%
        Memory Usage: 281.5 MB, less than 5.09%

        n == parent.length == s.length
        1 <= n <= 10^5
        0 <= parent[i] <= n - 1 for all i >= 1
        parent[0] == -1
        parent represents a valid tree.
        s consists of only lowercase English letters.
        """
        adj = collections.defaultdict(list)
        for i, p in enumerate(parent):
            adj[p].append(i)

        ret = 1

        def dp(pos) -> int:
            nonlocal ret
            if pos not in adj or not adj[pos]:
                return 1

            rets = [(dp(x), x) for x in adj[pos]]
            largest = heapq.nlargest(2, [x[0] for x in rets if s[x[1]] != s[pos]])
            if not largest:
                return 1
            ret = max(ret, sum(largest) + 1)
            return max(largest) + 1

        dp(0)

        return ret


def test():
    assert Solution().longestPath(parent=[-1, 0, 0, 1, 1, 2], s="abacbe") == 3


if __name__ == '__main__':
    test()
