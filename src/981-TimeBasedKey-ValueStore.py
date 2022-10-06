#!/usr/bin/env python3
"""
CREATED AT: 2022-10-06

URL: https://leetcode.com/problems/time-based-key-value-store/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 981-TimeBasedKey-ValueStore

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class TimeMap:
    """
    Runtime: 1442 ms, faster than 43.99%
    Memory Usage: 67.9 MB, less than 98.54%

    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 10^7
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 10^5 calls will be made to set and get
    """

    def __init__(self):
        self.root = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.root:
            self.root[key] = [[value], [timestamp]]
        else:
            self.root[key][0].append(value)
            self.root[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.root:
            return ""
        pos = bisect.bisect(self.root[key][1], timestamp)
        if pos == 0:
            return ""
        return self.root[key][0][pos - 1]


def test():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"


if __name__ == '__main__':
    test()
