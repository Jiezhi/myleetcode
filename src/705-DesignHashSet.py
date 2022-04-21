#!/usr/bin/env python
"""
CREATED AT: 2022/4/21
Des:
https://leetcode.com/problems/design-hashset/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class MyHashSet:
    """
    Runtime: 345 ms, faster than 41.94%
    Memory Usage: 45.5 MB, less than 5.31%

    0 <= key <= 10^6
    At most 10^4 calls will be made to add, remove, and contains.
    """

    def __init__(self):
        self.lst = [0] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.lst[key] = 1

    def remove(self, key: int) -> None:
        self.lst[key] = 0

    def contains(self, key: int) -> bool:
        return self.lst[key] == 1


def test():
    hash_set = MyHashSet()
    hash_set.add(1)
    hash_set.add(1000000)
    assert hash_set.contains(1)
    assert hash_set.contains(1000000)
    hash_set.remove(1)


if __name__ == '__main__':
    test()
