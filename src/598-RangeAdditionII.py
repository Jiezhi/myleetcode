#!/usr/bin/env python
"""
CREATED AT: 2021/8/30
Des:
https://leetcode.com/problems/range-addition-ii/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/617/week-5-august-29th-august-31st/3957/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """
        69 / 69 test cases passed.
        Status: Accepted
        Runtime: 64 ms
        Memory Usage: 16.1 MB
        :param m:
        :param n:
        :param ops:
        :return:
        """
        m_min, n_min = m, n
        for op in ops:
            m_min = min(op[0], m_min)
            n_min = min(op[1], n_min)
        return m_min * n_min


def test():
    assert Solution().maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]) == 4
    assert Solution().maxCount(m=3, n=3, ops=[[2, 3], [3, 2]]) == 4
    assert Solution().maxCount(
        m=3, n=3,
        ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
    ) == 4
    assert Solution().maxCount(m=3, n=3, ops=[]) == 9


if __name__ == '__main__':
    test()
