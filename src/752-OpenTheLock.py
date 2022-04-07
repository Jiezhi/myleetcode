#!/usr/bin/env python
"""
CREATED AT: 2022/4/7
Des:
https://leetcode.com/problems/open-the-lock/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        48 / 48 test cases passed.
        Status: Accepted
        Runtime: 1733 ms, faster than 16.76%
        Memory Usage: 16.5 MB

        1 <= deadends.length <= 500
        deadends[i].length == 4
        target.length == 4
        target will not be in the list deadends.
        target and deadends[i] consist of digits only.
        :param deadends:
        :param target:
        :return:
        """
        deadends = set(deadends)
        seen = set()

        dq = collections.deque([('0000', 0)])
        while dq:
            lock, cnt = dq.popleft()
            if lock == target:
                return cnt
            if lock in deadends or lock in seen:
                continue
            seen.add(lock)
            dq += [(f'{lock[:i]}{(int(lock[i]) + 1) % 10}{lock[i + 1:]}', cnt + 1) for i in range(4)]
            dq += [(f'{lock[:i]}{(int(lock[i]) + 9) % 10}{lock[i + 1:]}', cnt + 1) for i in range(4)]
        return -1


def test():
    pass


if __name__ == '__main__':
    test()
