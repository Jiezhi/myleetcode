#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:

https://leetcode.com/problems/ransom-note/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Runtime: 52 ms, faster than 89.71%
        Memory Usage: 14.1 MB, less than 95.18%

        1 <= ransomNote.length, magazine.length <= 10^5
        ransomNote and magazine consist of lowercase English letters.
        """
        cnt_note = collections.Counter(ransomNote)
        cnt_mag = collections.Counter(magazine)

        for k, v in cnt_note.items():
            if cnt_mag[k] < v:
                return False
        return True


def test():
    assert not Solution().canConstruct("a", "b")
    assert not Solution().canConstruct("aa", "ab")
    assert Solution().canConstruct("aa", "aab")


if __name__ == '__main__':
    test()
