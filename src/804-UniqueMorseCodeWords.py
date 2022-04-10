#!/usr/bin/env python
"""
CREATED AT: 2022/4/10
Des:

https://leetcode.com/problems/unique-morse-code-words/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Runtime: 51 ms, faster than 49.43%
        Memory Usage: 14 MB, less than 25.74%

        1 <= words.length <= 100
        1 <= words[i].length <= 12
        words[i] consists of lowercase English letters.
        :param words:
        :return:
        """
        MORSE_CODE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse_set = set()
        ORD_A = ord('a')
        for word in words:
            morse_set.add(''.join(MORSE_CODE[ord(c) - ORD_A] for c in word))
        return len(morse_set)


def test():
    assert Solution().uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]) == 2


if __name__ == '__main__':
    test()
