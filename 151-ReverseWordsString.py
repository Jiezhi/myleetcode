#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/12

Leetcode:
https://leetcode.com/problems/reverse-words-in-a-string/

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


def test():
    assert Solution().reverseWords('the sky is blue') == 'blue is sky the'
    assert Solution().reverseWords('  hello world!  ') == 'world! hello'
    assert Solution().reverseWords('a good   example') == 'example good a'


if __name__ == '__main__':
    test()