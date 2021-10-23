#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/12

Leetcode: https://leetcode.com/problems/reverse-words-in-a-string-iii/

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])


def test():
    assert Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"


if __name__ == '__main__':
    test()
