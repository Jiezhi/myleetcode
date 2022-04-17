#!/usr/bin/env python
"""
CREATED AT: 2022/4/17
Des:
https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        """
        1 <= total, cost1, cost2 <= 10^6
        :param total:
        :param cost1:
        :param cost2:
        :return:
        """
        ret = 0
        for i in range(total // cost1 + 1):
            ret += (total - i * cost1) // cost2 + 1
        return ret


def test():
    assert Solution().waysToBuyPensPencils(total=20, cost1=10, cost2=5) == 9
    assert Solution().waysToBuyPensPencils(total=5, cost1=10, cost2=10) == 1


if __name__ == '__main__':
    test()
