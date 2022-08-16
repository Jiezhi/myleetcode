#!/usr/bin/env python3
"""
CREATED AT: 2022-08-16

URL: https://leetcode.com/problems/design-an-ordered-stream/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1656-DesignAnOrderedStream

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class OrderedStream:
    """
    Runtime: 391 ms, faster than 28.54%
    Memory Usage: 14.9 MB, less than 11.88%

    1 <= n <= 1000
    1 <= id <= n
    value.length == 5
    value consists only of lowercase letters.
    Each call to insert will have a unique id.
    Exactly n calls will be made to insert.
    """

    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        ret = []
        while self.ptr < len(self.stream) and self.stream[self.ptr]:
            ret.append(self.stream[self.ptr])
            self.ptr += 1
        return ret


def test():
    os = OrderedStream(5)
    assert os.insert(3, "ccccc") == []
    assert os.insert(1, "aaaaa") == ['aaaaa']
    assert os.insert(2, "bbbbb") == ['bbbbb', 'ccccc']
    assert os.insert(5, "eeeee") == []
    assert os.insert(4, "ddddd") == ['ddddd', 'eeeee']


if __name__ == '__main__':
    test()
