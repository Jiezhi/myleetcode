#!/usr/bin/env python
"""
CREATED AT: 2022/1/3
Des:

https://leetcode.com/problems/find-the-town-judge/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Runtime: 1354 ms, faster than 5.04%
        Memory Usage: 18.8 MB, less than 97.64%

        1 <= n <= 1000
        0 <= trust.length <= 10^4
        trust[i].length == 2
        All the pairs of trust are unique.
        ai != bi
        1 <= ai, bi <= n
        :param n:
        :param trust:
        :return:
        """
        if n == 1 and not trust:
            return 1
        n_set = set(range(1, n + 1))
        trust_set = dict()
        for t in trust:
            if t[0] in n_set:
                n_set.remove(t[0])
            if t[1] not in trust_set:
                trust_set[t[1]] = 0
            trust_set[t[1]] += 1
        if len(n_set) == 1:
            ret = n_set.pop()
            if ret in trust_set and trust_set[ret] == n - 1:
                return ret
        return -1


def test():
    assert Solution().findJudge(n=1, trust=[]) == 1
    assert Solution().findJudge(n=2, trust=[[1, 2]]) == 2
    assert Solution().findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
    assert Solution().findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
    assert Solution().findJudge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3


if __name__ == '__main__':
    test()
