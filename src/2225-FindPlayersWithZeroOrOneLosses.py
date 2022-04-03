#!/usr/bin/env python
"""
CREATED AT: 2022/4/3
Des:
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_cnt = collections.Counter(x[0] for x in matches)
        lose_cnt = collections.Counter(x[1] for x in matches)
        win_ret = []
        for k in win_cnt.keys():
            if k not in lose_cnt or lose_cnt[k] == 0:
                win_ret.append(k)

        lose_ret = []
        for k, v in lose_cnt.items():
            if v == 1:
                lose_ret.append(k)
        return [sorted(win_ret), sorted(lose_ret)]


def test():
    assert Solution().findWinners(
        matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]) == [[1, 2, 10],
                                                                                                        [4, 5, 7, 8]]


if __name__ == '__main__':
    test()
