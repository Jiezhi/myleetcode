#!/usr/bin/env python3
"""
CREATED AT: 2022-09-13

URL: https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2047-NumberOfValidWordsInASentence

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def countValidWords(self, sentence: str) -> int:
        """
        Runtime: 69 ms, faster than 63.70%
        Memory Usage: 13.9 MB, less than 63.70%
        1 <= sentence.length <= 1000
        sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
        There will be at least 1 token.
        """
        ret = 0
        for token in sentence.split():
            hyphen = 0
            flag = False
            for i, c in enumerate(token[:-1]):
                if c == '-':
                    if i == 0 or hyphen > 0:
                        flag = True
                        break
                    else:
                        hyphen += 1
                elif c not in string.ascii_lowercase:
                    flag = True
                    break
            if flag:
                continue
            if token[-1] in string.ascii_lowercase:
                ret += 1
            elif hyphen == 1:
                if token[-2] != '-' and token[-1] in [',', '.', '!']:
                    ret += 1
            elif token[-1] in [',', '.', '!']:
                ret += 1
        return ret


def test():
    assert Solution().countValidWords(sentence="he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.") == 6
    assert Solution().countValidWords(sentence="!this  1-s b8d! q-.") == 0
    assert Solution().countValidWords(sentence="alice and  bob are playing stone-game10") == 5


if __name__ == '__main__':
    test()
