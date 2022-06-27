#!/usr/bin/env python
"""
CREATED AT: 2021/11/28
Des:

https://leetcode.com/problems/all-paths-from-source-to-target/
https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3849/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        CREATED AT: 2021/11/28
        Runtime: 116 ms, faster than 31.29%
        Memory Usage: 15.9 MB, less than 13.53%
        n == graph.length
        2 <= n <= 15
        0 <= graph[i][j] < n
        graph[i][j] != i (i.e., there will be no self-loops).
        All the elements of graph[i] are unique.
        The input graph is guaranteed to be a DAG.
        :param graph:
        :return:
        """
        n = len(graph)
        # build path matrix
        path_matrix = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                path_matrix[i][j] = True

        def get_path(target):
            rets = []
            if path_matrix[0][target]:
                rets.append([0, target])
            for i in range(1, n):
                if path_matrix[i][target]:
                    ret = get_path(target=i)
                    for r in ret:
                        r.append(target)
                        rets.append(r)

            return rets

        return get_path(n - 1)


def test():
    assert Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]


if __name__ == '__main__':
    test()
