#!/usr/bin/env python3
"""
CREATED AT: 2022-08-21

URL: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1455-CheckIfAWordOccursAsAPrefixOfAnyWordInASentence

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Runtime: 38 ms, faster than 76.69%
        Memory Usage: 13.8 MB, less than 59.60%
        
        1 <= sentence.length <= 100
        1 <= searchWord.length <= 10
        sentence consists of lowercase English letters and spaces.
        searchWord consists of lowercase English letters.
        """
        for i, s in enumerate(sentence.split(' '), 1):
            if s.startswith(searchWord):
                return i
        return -1


def test():
    assert Solution().isPrefixOfWord(sentence="i love eating burger", searchWord="burg") == 4
    assert Solution().isPrefixOfWord(sentence="this problem is an easy problem", searchWord="pro") == 2


if __name__ == '__main__':
    test()
