#!/usr/bin/env python3
"""
CREATED AT: 2022-09-18

URL: https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2414-LengthOfTheLongestAlphabeticalContinuousSubstring

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        """
        1 <= s.length <= 10^5
        s consists of only English lowercase letters.
        """
        ret = 1
        p, pre = 0, s[0]
        for pos, c in enumerate(s, 1):
            if ord(c) - ord(pre) == 1:
                pre = c
                continue
            else:
                ret = max(ret, pos - p)
                if ret == 26:
                    return ret
                pre = c
                p = pos
        ret = max(ret, pos - p + 1)
        return ret


def test():
    assert Solution().longestContinuousSubstring(s="abacaba") == 2
    assert Solution().longestContinuousSubstring(s="abcde") == 5


if __name__ == '__main__':
    test()
