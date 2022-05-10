#!/usr/bin/env python
"""
CREATED AT: 2022/5/10
Des:
https://leetcode.com/problems/combination-sum-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 39 -> 40 -> 77 -> 78 -> 90 -> 216

"""
import collections
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        AC: 05/10/2022
        Runtime: 26 ms, faster than 98.07%
        Memory Usage: 13.9 MB, less than 29.87%
        :param k: 2 <= k <= 9
        :param n: 1 <= n <= 60
        :return:
        """
        if n < (k + 1) * k // 2 or n > sum(x for x in range(9 - k + 1, 10)):
            return []
        dq = collections.deque(([x], x) for x in range(1, 10))
        ret = []
        while dq:
            node, total = dq.popleft()
            if len(node) > k or total > n:
                continue
            if len(node) == k and total == n:
                ret.append(node)
                continue
            for num in range(node[-1] + 1, 10):
                dq.append((node + [num], total + num))
        return ret


def test():
    assert Solution().combinationSum3(3, 7) == [[1, 2, 4]]


if __name__ == '__main__':
    test()
