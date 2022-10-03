#!/usr/bin/env python3
"""
CREATED AT: 2022-10-03

URL: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1784-CheckIfBinaryStringHasAtMostOneSegmentOfOnes

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """
        Runtime: 65 ms, faster than 15.78%
        Memory Usage: 13.9 MB, less than 8.94%

        1 <= s.length <= 100
        s[i] is either '0' or '1'.
        s[0] is '1'.
        """
        i, j = 0, len(s) - 1
        while i <= j and s[i] == '0':
            i += 1
        if i > j:
            return True
        while j >= i and s[j] == '0':
            j -= 1
        while i <= j:
            if s[i] == '0':
                return False
            i += 1
        return True


def test():
    assert not Solution().checkOnesSegment(s="1001")
    assert Solution().checkOnesSegment(s="110")


if __name__ == '__main__':
    test()
