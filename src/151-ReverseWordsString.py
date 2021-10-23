#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/9/12
Updated on 2021/10/20

Leetcode: https://leetcode.com/problems/reverse-words-in-a-string/

Difficulty: Medium

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Runtime: 28 ms, faster than 91.83%
        Memory Usage: 14.3 MB, less than 86.72%

        :param s:
        :return:
        """
        return ' '.join(reversed(s.split()))

    def reverseWords2(self, s: str) -> str:
        """
        reverse in-place,
        str in python is immutable, so we convert str to char list instead
        1 <= s.length <= 10**4
        s contains English letters (upper-case and lower-case), digits, and spaces ' '.
        There is at least one word in s
        :param s:
        :return:
        """
        s = list(s)
        l, h = 0, len(s) - 1
        # reverse string
        while l < h:
            s[l], s[h] = s[h], s[l]
            l += 1
            h -= 1
        # reverse words
        l = 0
        while l < len(s):
            if l != ' ':
                h = l + 1
                while h < len(s) and s[h] != ' ':
                    h += 1
                # reverse from l to h - 1
                tmp_h = h - 1
                while l < tmp_h:
                    s[l], s[tmp_h] = s[tmp_h], s[l]
                    l += 1
                    tmp_h -= 1
                l = h + 1
            else:
                l += 1

        # remove extra spaces
        space_cnt = 0
        l = 0
        while l < len(s):
            if s[l] == ' ':
                space_cnt += 1
            elif space_cnt > 1:
                for i in range(l, len(s)):
                    s[i - space_cnt + 1] = s[i]
                for i in range(len(s) - space_cnt + 1, len(s)):
                    s[i] = ' '
                l = l - space_cnt
                space_cnt = 0
            else:
                space_cnt = 0
            l += 1

        l = 0
        while s[l] == ' ':
            l += 1
        h = len(s) - 1
        while s[h] == ' ':
            h -= 1
        return ''.join(s[l:h + 1])


def test():
    assert Solution().reverseWords2("F R  I   E    N     D      S      ") == "S D N E I R F"
    assert Solution().reverseWords('the sky is blue') == 'blue is sky the'
    assert Solution().reverseWords('  hello world!  ') == 'world! hello'
    assert Solution().reverseWords('a good   example') == 'example good a'

    assert Solution().reverseWords2('the sky is blue') == 'blue is sky the'
    assert Solution().reverseWords2('  hello world!  ') == 'world! hello'
    assert Solution().reverseWords2('a good   example') == 'example good a'


if __name__ == '__main__':
    test()
