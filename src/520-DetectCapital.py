#!/usr/bin/env python
"""
CREATED AT: 2022/1/24
Des:

https://leetcode.com/problems/detect-capital/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Runtime: 28 ms, faster than 91.10%
        Memory Usage: 14.2 MB, less than 46.33%
        1 <= word.length <= 100
        word consists of lowercase and uppercase English letters.
        :param word:
        :return:
        """
        # return word in [word.lower(), word.upper(), word.capitalize()]
        return word.islower() or word.isupper() or word.istitle()


def test():
    assert Solution().detectCapitalUse(word="USA")
    assert not Solution().detectCapitalUse(word="FlaG")


if __name__ == '__main__':
    test()
