#!/usr/bin/env python3
"""
CREATED AT: 2022-10-09

URL: https://leetcode.com/contest/weekly-contest-314/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2434-UsingARobotToPrintTheLexicographicallySmallestString

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def robotWithString(self, s: str) -> str:
        """
        1 <= s.length <= 10^5
        s consists of only English lowercase letters.
        """
        t, p = [], []
        stack = [s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if s[i] <= stack[-1]:
                stack.append(s[i])
            else:
                stack.append(stack[-1])

        for c in s:
            while t and t[-1] <= stack[-1]:
                p.append(t.pop())
            if c == stack[-1]:
                p.append(c)
            else:
                t.append(c)
            stack.pop()

        return ''.join(p) + ''.join(t[::-1])


def test():
    assert Solution().robotWithString(s="zza") == "azz"
    assert Solution().robotWithString(s="bac") == "abc"
    assert Solution().robotWithString(s="bdda") == "addb"


if __name__ == '__main__':
    test()
