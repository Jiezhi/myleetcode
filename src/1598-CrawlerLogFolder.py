#!/usr/bin/env python3
"""
CREATED AT: 2022-09-09

URL: https://leetcode.com/problems/crawler-log-folder/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1598-CrawlerLogFolder

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        """
        Runtime: 45 ms, faster than 96.52%
        Memory Usage: 14.2 MB, less than 38.05%

        1 <= logs.length <= 10^3
        2 <= logs[i].length <= 10
        logs[i] contains lowercase English letters, digits, '.', and '/'.
        logs[i] follows the format described in the statement.
        Folder names consist of lowercase English letters and digits.
        """
        ret = 0
        for op in logs:
            if op == '../':
                ret = max(0, ret - 1)
            elif op == './':
                continue
            else:
                ret += 1
        return ret


def test():
    assert Solution().minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]) == 2
    assert Solution().minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3
    assert Solution().minOperations(logs=["d1/", "../", "../", "../"]) == 0


if __name__ == '__main__':
    test()
