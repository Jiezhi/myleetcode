#!/usr/bin/env python
"""
CREATED AT: 2022/2/7
Des:

https://leetcode.com/problems/network-delay-time/
https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3863/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        CREATED AT: 2022/2/7
        52 / 52 test cases passed.
        Status: Accepted
        Runtime: 635 ms, faster than 49.94%
        Memory Usage: 16.7 MB, less than 11.28%
        1 <= k <= n <= 100
        1 <= times.length <= 6000
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        0 <= wi <= 100
        All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
        :param times:
        :param n:
        :param k:
        :return:
        """
        # nodes are labeled from 1 to n
        cost = [sys.maxsize] * (n + 1)
        cost[k] = 0
        time_dict = collections.defaultdict(list)
        for u, v, t in times:
            time_dict[u].append((v, t))
        dq = collections.deque()
        dq.append(k)
        visited = set()
        while dq:
            u = dq.popleft()
            if u in visited:
                continue
            visited.add(u)
            for v, t in time_dict[u]:
                if cost[u] + t < cost[v]:
                    cost[v] = cost[u] + t
                    if v in visited:
                        visited.remove(v)
                if v not in visited:
                    dq.append(v)

        ret = max(cost[1:])
        return ret if ret != sys.maxsize else -1


def test():
    assert Solution().networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=2, k=2) == 3
    assert Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2) == 2
    assert Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=1) == -1
    assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1) == 1
    assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2) == -1


if __name__ == '__main__':
    test()
