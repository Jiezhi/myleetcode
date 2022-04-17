#!/usr/bin/env python
"""
CREATED AT: 2022/4/17
Des:
https://leetcode.com/problems/design-an-atm-machine/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class ATM:

    def __init__(self):
        self.cnt = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, v in enumerate(banknotesCount):
            self.cnt[i] += v

    def withdraw(self, amount: int) -> List[int]:
        counts = [20, 50, 100, 200, 500]
        cur_cnt = self.cnt.copy()
        ret = [0] * 5
        for i in range(4, -1, -1):
            ret[i] = min(self.cnt[i], amount // counts[i])
            self.cnt[i] -= ret[i]
            amount -= counts[i] * ret[i]
        if amount:
            self.cnt = cur_cnt
            return [-1]

        return ret


def test():
    atm = ATM()
    atm.deposit([0, 0, 1, 2, 1])
    assert atm.withdraw(600) == [0, 0, 1, 0, 1]
    atm.deposit([0, 1, 0, 1, 1])
    assert atm.withdraw(600) == [-1]
    assert atm.withdraw(550) == [0, 1, 0, 0, 1]


if __name__ == '__main__':
    test()
