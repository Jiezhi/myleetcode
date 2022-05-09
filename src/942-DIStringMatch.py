#!/usr/bin/env python
"""
CREATED AT: 2022/5/9
Des:
https://leetcode.com/problems/di-string-match/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """
        Runtime: 100 ms, faster than 36.29%
        Memory Usage: 15.3 MB, less than 45.65%
        :param s: 1 <= s.length <= 10^5
               s[i] is either 'I' or 'D'.
        :return:
        """
        i, j = 0, len(s)
        ret = []
        for c in s:
            if c == 'I':
                ret.append(i)
                i += 1
            else:
                ret.append(j)
                j -= 1
        return ret + [i]


def test():
    assert Solution().diStringMatch("IDID") == [0, 4, 1, 3, 2]


if __name__ == '__main__':
    test()
