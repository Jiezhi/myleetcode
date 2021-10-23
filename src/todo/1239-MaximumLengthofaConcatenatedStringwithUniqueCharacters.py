#!/usr/bin/env python
"""
CREATED AT: 2021/9/22
Des:
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
https://leetcode.com/explore/item/3984
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        pass


def test():
    assert Solution().maxLength(arr=["un", "iq", "ue"]) == 4
    assert Solution().maxLength(arr=["cha", "r", "act", "ers"]) == 6
    assert Solution().maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]) == 26


if __name__ == '__main__':
    test()
