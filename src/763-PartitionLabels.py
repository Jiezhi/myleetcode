#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:
https://leetcode.com/problems/partition-labels/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Runtime: 54 ms, faster than 60.28%
        Memory Usage: 14 MB, less than 36.30%

        1 <= s.length <= 500
        s consists of lowercase English letters.
        """
        if not s:
            return None
        rpos = s.rfind(s[0])

        i = 1
        while i < rpos:
            r = s.rfind(s[i], rpos + 1)
            if r == -1:
                i += 1
            else:
                rpos = r
        if rpos == len(s) - 1:
            return [rpos + 1]
        else:
            return [rpos + 1] + self.partitionLabels(s[rpos + 1:])


def test():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert Solution().partitionLabels("a") == [1]


if __name__ == '__main__':
    test()
