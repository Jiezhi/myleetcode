#!/usr/bin/env python3
"""
CREATED AT: 2022-09-07

URL: https://leetcode.com/problems/rearrange-spaces-between-words/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1592-RearrangeSpacesBetweenWords

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        """
        Runtime: 52 ms, faster than 35.65%
        Memory Usage: 13.9 MB, less than 16.35%

        1 <= text.length <= 100
        text consists of lowercase English letters and ' '.
        text contains at least one word.
        """
        words = text.split()
        space_cnt = text.count(' ')
        if space_cnt == 0:
            return text
        if len(words) == 1:
            return words[0] + ' ' * space_cnt
        space, left = divmod(space_cnt, len(words) - 1)
        return (' ' * space).join(words) + ' ' * left


def test():
    assert Solution().reorderSpaces(text="a") == "a"
    assert Solution().reorderSpaces(text=" a ") == "a  "
    assert Solution().reorderSpaces(text="  this   is  a sentence ") == "this   is   a   sentence"
    assert Solution().reorderSpaces(text=" practice   makes   perfect") == "practice   makes   perfect "


if __name__ == '__main__':
    test()
