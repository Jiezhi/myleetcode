#!/usr/bin/env python
"""
CREATED AT: 2022/5/7
Des:
https://leetcode.com/problems/minimum-genetic-mutation/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        Runtime: 46 ms, faster than 42.52%
        Memory Usage: 13.8 MB, less than 89.39%
        start.length == 8
        end.length == 8
        0 <= bank.length <= 10
        bank[i].length == 8
        start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
        :param start:
        :param end:
        :param bank:
        :return:
        """
        if start == end:
            return 0
        if end not in bank:
            return -1
        gene = ['A', 'C', 'G', 'T']
        bank = set(bank)
        dq = collections.deque([(start, 0)])
        while dq:
            node, cnt = dq.popleft()
            for i in range(8):
                for g in gene:
                    new_node = f'{node[:i]}{g}{node[i + 1:]}'
                    if new_node == end:
                        return cnt + 1
                    if new_node in bank:
                        dq.append((new_node, cnt + 1))
                        bank.remove(new_node)
        return -1


def test():
    assert Solution().minMutation(start="AACCGGTT", end="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2


if __name__ == '__main__':
    test()
