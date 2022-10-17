#!/usr/bin/env python3
"""
CREATED AT: 2022-10-17

URL: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1832-CheckIfTheSentenceIsPangram

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Runtime: 27 ms, faster than 98.00%
        Memory Usage: 13.8 MB, less than 95.55%
        
        1 <= sentence.length <= 1000
        sentence consists of lowercase English letters.
        """
        return len(sentence) >= 26 and len(Counter(sentence)) == 26


def test():
    assert Solution().checkIfPangram(sentence="thequickbrownfoxjumpsoverthelazydog")
    assert not Solution().checkIfPangram(sentence="leetcode")


if __name__ == '__main__':
    test()
