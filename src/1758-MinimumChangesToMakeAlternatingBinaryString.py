#!/usr/bin/env python3
"""
CREATED AT: 2022-11-29

URL: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1758-MinimumChangesToMakeAlternatingBinaryString

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def minOperations(self, s: str) -> int:
        """
        1 <= s.length <= 10^4
        s[i] is either '0' or '1'.
        """
        # ret1 for start with 0
        # ret2 for start with 1
        ret1, ret2 = 0, 0
        for i, c in enumerate(s):
            if i & 1:
                if c == '1':
                    ret2 += 1
                else:
                    ret1 += 1
            elif c == '1':
                ret1 += 1
            else:
                ret2 += 1
        return min(ret1, ret2)


def test():
    assert Solution().minOperations(s="0100") == 1
    assert Solution().minOperations(s="10") == 0
    assert Solution().minOperations(s="1111") == 2


if __name__ == '__main__':
    test()
