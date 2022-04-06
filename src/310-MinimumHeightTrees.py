#!/usr/bin/env python
"""
CREATED AT: 2022/2/9
Des:

https://leetcode.com/problems/minimum-height-trees/
https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3953/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Ref: https://leetcode.com/problems/minimum-height-trees/solution/

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        CREATED AT: 2022/4/6
        Runtime: 128 ms, faster than 83.86%
        Memory Usage: 26.7 MB, less than 8.64%
        :param n:
        :param edges:
        :return:
        """
        if n == 1:
            return [0]
        cnt = [0] * n
        adj = collections.defaultdict(set)

        for x, y in edges:
            cnt[x] += 1
            cnt[y] += 1
            adj[x].add(y)
            adj[y].add(x)

        dq = [i for i in range(n) if cnt[i] == 1]
        remain = n
        while remain > 2:
            remain -= len(dq)
            tmp_dq = dq
            dq = []
            for v in tmp_dq:
                for node in adj[v]:
                    cnt[node] -= 1
                    if cnt[node] == 1:
                        dq.append(node)
        return dq

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        CREATED AT: 2022/2/9
        71 / 71 test cases passed.
        Status: Accepted
        Runtime: 960 ms, faster than 12.51%
        Memory Usage: 25.1 MB, less than 30.75%
        1 <= n <= 2 * 10^4
        edges.length == n - 1
        0 <= a_i, b_i < n
        a_i != b_i
        All the pairs (a_i, b_i) are distinct.
        The given input is guaranteed to be a tree and there will be no repeated edges.
        :param n:
        :param edges:
        :return:
        """
        if n == 1:
            return [0]
        relations = [set() for _ in range(n)]
        for edge in edges:
            relations[edge[0]].add(edge[1])
            relations[edge[1]].add(edge[0])
        leaves = []
        for i in range(n):
            if len(relations[i]) == 1:
                leaves.append(i)
        remain_cnt = n
        while remain_cnt > 2:
            remain_cnt -= len(leaves)
            new_leaves = []
            for leaf_id in leaves:
                leaf = relations[leaf_id].pop()
                relations[leaf].remove(leaf_id)
                if len(relations[leaf]) == 1:
                    new_leaves.append(leaf)
            leaves = new_leaves
        return leaves


def test():
    assert Solution().findMinHeightTrees(n=5, edges=[[0, 1], [0, 2], [0, 3], [3, 4]]) == [0, 3]
    assert Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]) == [1]
    assert Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]) in [[3, 4], [4, 3]]
    assert Solution().findMinHeightTrees(n=1, edges=[]) == [0]
    assert Solution().findMinHeightTrees(n=2, edges=[[0, 1]]) in [[0, 1], [1, 0]]
    assert Solution().findMinHeightTrees(n=3, edges=[[0, 1], [1, 2]]) == [1]


if __name__ == '__main__':
    test()
