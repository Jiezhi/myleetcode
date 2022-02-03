#!/usr/bin/env python
"""
CREATED AT: 2022/1/8
Des:

https://leetcode.com/problems/capitalize-the-title
https://leetcode.com/contest/biweekly-contest-69/problems/capitalize-the-title/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        """
        1 <= title.length <= 100
        title consists of words separated by a single space without any leading or trailing spaces.
        Each word consists of uppercase and lowercase English letters and is non-empty.
        :param title:
        :return:
        """
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) < 3:
                words[i] = words[i].lower()
            else:
                words[i] = words[i].capitalize()
        return ' '.join(words)


def test():
    assert Solution().capitalizeTitle(title="capiTalIze tHe titLe") == "Capitalize The Title"


if __name__ == '__main__':
    test()
