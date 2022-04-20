#!/usr/bin/env python
"""
Created on 2019/9/12

Leetcode: https://leetcode.com/problems/reverse-words-in-a-string-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        1 <= s.length <= 5 * 10^4
        s contains printable ASCII characters.
        s does not contain any leading or trailing spaces.
        There is at least one word in s.
        All the words in s are separated by a single space.
        :param s:
        :return:
        """
        return ' '.join([x[::-1] for x in s.split()])


def test():
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"


if __name__ == '__main__':
    test()
