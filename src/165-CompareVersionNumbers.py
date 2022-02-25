#!/usr/bin/env python
"""
CREATED AT: 2022/2/25
Des:

https://leetcode.com/problems/compare-version-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Runtime: 28 ms, faster than 93.87%
        Memory Usage: 14 MB, less than 52.71%

        1 <= version1.length, version2.length <= 500
        version1 and version2 only contain digits and '.'.
        version1 and version2 are valid version numbers.
        All the given revisions in version1 and version2 can be stored in a 32-bit integer.
        """
        if version1 == version2:
            return 0
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        if len(v2) == len(v1):
            return 0
        elif len(v2) < len(v1):
            if any(x > 0 for x in v1[len(v2):]):
                return 1
            else:
                return 0
        else:
            return -1 if any(x > 0 for x in v2[len(v1):]) else 0


def test():
    assert Solution().compareVersion("1.0", "1") == 0
    assert Solution().compareVersion("1", "1.1") == -1


if __name__ == '__main__':
    test()
