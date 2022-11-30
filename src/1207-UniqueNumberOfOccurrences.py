#!/usr/bin/env python3
"""
CREATED AT: 2022-11-30

URL: https://leetcode.com/problems/unique-number-of-occurrences/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1207-UniqueNumberOfOccurrences

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Runtime: 79 ms, faster than 21.81%
        Memory Usage: 13.9 MB, less than 72.74%
        1 <= arr.length <= 1000
        -1000 <= arr[i] <= 1000
        """
        cnt = Counter(arr)
        return len(cnt.keys()) == len(set(cnt.values()))


def test():
    assert Solution().uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3])
    assert not Solution().uniqueOccurrences(arr=[1, 2])
    assert Solution().uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0])


if __name__ == '__main__':
    test()
