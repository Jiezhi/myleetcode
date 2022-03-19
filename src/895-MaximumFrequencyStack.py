#!/usr/bin/env python
"""
CREATED AT: 2022/3/19
Des:
https://leetcode.com/problems/maximum-frequency-stack/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
import collections


class FreqStack:
    """
    Runtime: 600 ms, faster than 14.99%
    Memory Usage: 22.7 MB, less than 47.51%

    0 <= val <= 10^9
    At most 2 * 10^4 calls will be made to push and pop.
    It is guaranteed that there will be at least one element in the stack before calling pop.
    """

    def __init__(self):
        self.cnt = collections.defaultdict(int)
        self.cnt_list = collections.defaultdict(list)
        self.max_key = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.cnt_list[self.cnt[val]].append(val)
        self.max_key = max(self.max_key, self.cnt[val])

    def pop(self) -> int:
        val = self.cnt_list[self.max_key].pop()
        self.cnt[val] -= 1
        if not self.cnt_list[self.max_key]:
            self.max_key -= 1
        return val


def test():
    freq = FreqStack()
    freq.push(5)
    freq.push(7)
    freq.push(5)
    freq.push(7)
    freq.push(4)
    freq.push(5)

    assert freq.pop() == 5
    assert freq.pop() == 7
    assert freq.pop() == 5
    assert freq.pop() == 4


if __name__ == '__main__':
    test()
