#!/usr/bin/env python
"""
CREATED AT: 2022/4/21
Des:
https://leetcode.com/problems/goat-latin/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        Runtime: 24 ms, faster than 99.00%
        Memory Usage: 13.9 MB, less than 66.54%

        1 <= sentence.length <= 150
        sentence consists of English letters and spaces.
        sentence has no leading or trailing spaces.
        All the words in sentence are separated by a single space.
        """
        ret = []
        for i, word in enumerate(sentence.split(' ')):
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                ret.append(f'{word}ma{"a" * (i + 1)}')
            else:
                ret.append(f'{word[1:]}{word[0]}ma{"a" * (i + 1)}')
        return ' '.join(ret)


def test():
    assert Solution().toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


if __name__ == '__main__':
    test()
