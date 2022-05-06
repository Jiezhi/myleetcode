#!/usr/bin/env python
"""
CREATED AT: 2022/5/6
Des:
https://leetcode.com/problems/number-of-recent-calls/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import collections


class RecentCounter:
    """
    Runtime: 316 ms, faster than 69.02%
    Memory Usage: 19.5 MB, less than 69.27%
    1 <= t <= 10^9
    Each test case will call ping with strictly increasing values of t.
    At most 10^4 calls will be made to ping.
    """
    def __init__(self):
        self.dq = collections.deque()

    def ping(self, t: int) -> int:
        self.dq.append(t)
        while self.dq[0] + 3000 < t:
            self.dq.popleft()
        return len(self.dq)


def test():
    cnt = RecentCounter()
    assert cnt.ping(1) == 1
    assert cnt.ping(100) == 2
    assert cnt.ping(3001) == 3
    assert cnt.ping(3002) == 3


if __name__ == '__main__':
    test()
