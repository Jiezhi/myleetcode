#!/usr/bin/env python
"""
CREATED AT: 2022/4/1
Des:
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        """
        Runtime: 36 ms, faster than 76.12%
        Memory Usage: 13.9 MB, less than 21.49%

        1 <= s.length <= 1000
        s consists of digits and the '#' letter.
        s will be a valid string such that mapping is always possible.
        :param s:
        :return:
        """
        ret = []
        i = 0
        base_ord = ord('a') - 1
        while i < len(s) - 2:
            if s[i] in ['1', '2'] and s[i + 2] == '#':
                ret.append(chr(base_ord + int(s[i:i + 2])))
                i += 3
            else:
                ret.append(chr(base_ord + int(s[i])))
                i += 1
        if i < len(s):
            ret.append(chr(base_ord + int(s[i])))
        if i < len(s) - 1:
            ret.append(chr(base_ord + int(s[i + 1])))
        return ''.join(ret)


def test():
    assert Solution().freqAlphabets(s="10#11#12") == "jkab"


if __name__ == '__main__':
    test()
