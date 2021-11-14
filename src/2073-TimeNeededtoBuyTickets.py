#!/usr/bin/env python
"""
CREATED AT: 2021/11/14
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        n == tickets.length
        1 <= n <= 100
        1 <= tickets[i] <= 100
        0 <= k < n
        :param tickets:
        :param k:
        :return:
        """
        ret = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    ret += 1
                if i == k and tickets[k] == 0:
                    break
        return ret


def test():
    assert Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2) == 6
    assert Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0) == 8


if __name__ == '__main__':
    test()
