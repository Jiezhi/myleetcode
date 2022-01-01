#!/usr/bin/env python
"""
CREATED AT: 2022/1/1
Des:

https://leetcode.com/problems/keyboard-row/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Runtime: 34 ms, faster than 17.92%
        Memory Usage: 14.4 MB, less than 16.88%
        2022/1/1
        1 <= words.length <= 20
        1 <= words[i].length <= 100
        words[i] consists of English letters (both lowercase and uppercase).
        :param words:
        :return:
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        ret = []
        for word in words:
            if not word:
                continue
            w = word[0].lower()
            if w in row1:
                row = row1
            elif w in row2:
                row = row2
            elif w in row3:
                row = row3
            else:
                raise RuntimeError(f'unknown char {word[0]}')
            err = False
            for w in word[1:]:
                if w.lower() not in row:
                    err = True
                    break
            if err:
                continue
            else:
                ret.append(word)
        return ret


def test():
    assert Solution().findWords(words=["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    assert Solution().findWords(words=["adsdf", "sfd"]) == ["adsdf", "sfd"]


if __name__ == '__main__':
    test()
