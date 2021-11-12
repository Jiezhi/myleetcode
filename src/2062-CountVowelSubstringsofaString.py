#!/usr/bin/env python
"""
CREATED AT: 2021/11/7
Des:

https://leetcode.com/problems/count-vowel-substrings-of-a-string
https://leetcode.com/contest/weekly-contest-266/problems/count-vowel-substrings-of-a-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        """
        1 <= word.length <= 100
        word consists of lowercase English letters only.
        :param word:
        :return:
        """
        ret = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(word)):
            if word[i] not in vowel:
                continue
            wd = defaultdict(int)
            wd[word[i]] += 1
            for j in range(i + 1, len(word)):
                if word[j] not in vowel:
                    break
                wd[word[j]] += 1
                if len(wd) >= 5:
                    ret += 1
        return ret


def test():
    assert Solution().countVowelSubstrings(word="duuebuaeeeeeeuaoeiueaoui") == 81
    assert Solution().countVowelSubstrings(word="cuaieuouac") == 7
    assert Solution().countVowelSubstrings(word="aeiouu") == 2
    assert Solution().countVowelSubstrings(word="a") == 0
    assert Solution().countVowelSubstrings(word="unicornarihan") == 0


if __name__ == '__main__':
    test()
