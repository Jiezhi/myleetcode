#!/usr/bin/env python
"""
CREATED AT: 2022/2/20
Des:

https://leetcode.com/problems/construct-string-with-repeat-limit/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """
        150 / 150 test cases passed.
        Status: Accepted
        Runtime: 5072 ms
        Memory Usage: 16.2 MB
        1 <= repeatLimit <= s.length <= 10^5
        s consists of lowercase English letters.
        """
        cnts = [0] * 26
        ord_a = ord('a')
        for c in s:
            cnts[ord(c) - ord_a] += 1
        ret = []
        curr_repeat = 0
        pre_len = -1
        pre_char = None
        while len(ret) != pre_len:
            pre_len = len(ret)
            for i in range(25, -1, -1):
                c = chr(ord_a + i)
                if c == pre_char and curr_repeat >= repeatLimit:
                    continue
                if cnts[i] > 0:
                    ret.append(c)
                    cnts[i] -= 1
                    if c == pre_char:
                        curr_repeat += 1
                    else:
                        pre_char = c
                        curr_repeat = 1
                    break
        return ''.join(ret)


def test():
    assert Solution().repeatLimitedString(s="cczazcc", repeatLimit=3) == "zzcccac"


if __name__ == '__main__':
    test()
