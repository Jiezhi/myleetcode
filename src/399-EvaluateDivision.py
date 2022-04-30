#!/usr/bin/env python
"""
CREATED AT: 2022/2/10
Des:

https://leetcode.com/problems/evaluate-division/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        AC: 04/30/2022 20:53
        Runtime: 31 ms, faster than 88.83%
        Memory Usage: 14 MB, less than 16.96%

        1 <= equations.length <= 20
        equations[i].length == 2
        1 <= Ai.length, Bi.length <= 5
        values.length == equations.length
        0.0 < values[i] <= 20.0
        1 <= queries.length <= 20
        queries[i].length == 2
        1 <= Cj.length, Dj.length <= 5
        Ai, Bi, Cj, Dj consist of lower case English letters and digits.
        Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero
        and that there is no contradiction.
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        adj = collections.defaultdict(list)
        for i, (f, t) in enumerate(equations):
            adj[f].append((t, values[i]))
            adj[t].append((f, 1 / values[i]))
        ret = []
        for a, b in queries:
            if a not in adj or b not in adj:
                ret.append(-1.0)
            elif a == b:
                ret.append(1.0)
            else:
                seen = set()
                seen.add(a)
                dq = collections.deque(adj[a])
                found = False
                while dq:
                    c, cost = dq.popleft()
                    if c in seen:
                        continue
                    if c == b:
                        ret.append(cost)
                        found = True
                        break
                    seen.add(c)
                    dq += [(x, y * cost) for x, y in adj[c]]
                if not found:
                    ret.append(-1.0)
        return ret


def test():
    assert Solution().calcEquation(
        equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
        queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ) == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    assert Solution().calcEquation(
        equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
        queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    ) == [3.75000, 0.40000, 5.00000, 0.20000]

    assert Solution().calcEquation(
        equations=[["a", "b"]], values=[0.5],
        queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    ) == [0.50000, 2.00000, -1.00000, -1.00000]


if __name__ == '__main__':
    test()
