#!/usr/bin/env python
"""
CREATED AT: 2021/9/8
Des:
https://leetcode.com/problems/shifting-letters
https://leetcode.com/explore/item/3968
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        53 / 53 test cases passed.
        Status: Accepted
        Runtime: 4441 ms
        Memory Usage: 28.1 MB
        :param s:
        :param shifts:
        :return:
        """
        shift_cnt = 0
        ret = ''
        for i in range(1, len(s) + 1):
            shift_cnt += shifts[-i]
            shift_cnt %= 26
            k = ord(s[-i]) + shift_cnt
            # ord('z') = 122
            if k > 122:
                k -= 26
            ret = chr(k) + ret
        return ret


def test():
    assert Solution().shiftingLetters("ruu", [26, 9, 17]) == "rul"
    assert Solution().shiftingLetters(s="abc", shifts=[3, 5, 9]) == "rpl"
    assert Solution().shiftingLetters(s="aaa", shifts=[1, 2, 3]) == "gfd"


if __name__ == '__main__':
    test()
