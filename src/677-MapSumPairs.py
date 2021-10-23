#!/usr/bin/env python
"""
CREATED AT: 2021/10/8
Des:

https://leetcode.com/problems/map-sum-pairs/
https://leetcode.com/explore/learn/card/trie/148/practical-application-i/1058/
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3832/
GITHUB: https://github.com/Jiezhi/myleetcode

See: 208
"""
import collections


class MapSum:
    """
    35 / 35 test cases passed.
    Status: Accepted
    Runtime: 28 ms
    Memory Usage: 14.4 MB

    Runtime: 28 ms, faster than 89.65% of Python3 online submissions for Map Sum Pairs.
    Memory Usage: 14.4 MB, less than 25.00% of Python3 online submissions for Map Sum Pairs.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        """
        Inserts the key-val pair into the map.
        If the key already existed, the original key-value pair
        will be overridden to the new one.
        :param key:
        :param val:
        :return:
        """
        cur = self.root
        for c in key:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        # set the word value at the last character.
        cur['val'] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur:
                return 0
            cur = cur[c]
        ret = 0
        # add all children values
        dq = collections.deque()
        dq.append(cur)
        while len(dq) > 0:
            cur = dq.pop()
            if 'val' in cur:
                ret += cur['val']
            [dq.append(x) for k, x in cur.items() if k != 'val']
        return ret


def test():
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    assert mapSum.sum("ap") == 3  # return 3 (apple=3)
    mapSum.insert("app", 2)
    assert mapSum.sum("ap") == 5  # return 5 (apple + app = 3 + 2 = 5)


if __name__ == '__main__':
    test()
