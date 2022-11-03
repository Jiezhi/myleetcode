#!/usr/bin/env python3
"""
CREATED AT: 2022-11-03

URL: https://leetcode.com/problems/maximum-repeating-substring/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1668-MaximumRepeatingSubstring

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        """
        212 / 212 test cases passed.
        Runtime: 46 ms
        Memory Usage: 13.9 MB
        1 <= sequence.length <= 100
        1 <= word.length <= 100
        sequence and word contains only lowercase English letters.
        """
        if word not in sequence:
            return 0
        ret = 0
        tmp = word
        while len(tmp) <= len(sequence) and tmp in sequence:
            ret += 1
            tmp = word * ret
        return ret - 1


def test():
    assert Solution().maxRepeating(sequence="ababc", word="ab") == 2
    assert Solution().maxRepeating(sequence="ababc", word="ba") == 1
    assert Solution().maxRepeating(sequence="ababc", word="ac") == 0


if __name__ == '__main__':
    test()
