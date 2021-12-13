#!/usr/bin/env python
"""
CREATED AT: 2021/12/13
Des:

https://leetcode.com/problems/consecutive-characters/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent: 6 min
"""


class Solution:
    def maxPower(self, s: str) -> int:
        """
        Runtime: 40 ms, faster than 81.15% of Python3
        Memory Usage: 14 MB, less than 89.89% of Python3
        :param s: 1 <= s.length <= 500
        s consists of only lowercase English letters.
        :return:
        """
        if not s:
            return 0

        tmp_c = s[0]
        ret = 1
        tmp_ret = 1
        for c in s[1:]:
            if c == tmp_c:
                tmp_ret += 1
            else:
                ret = max(ret, tmp_ret)
                tmp_ret = 1
                tmp_c = c
        ret = max(ret, tmp_ret)
        return ret


def test():
    assert Solution().maxPower(s="l") == 1
    assert Solution().maxPower(s="cc") == 2
    assert Solution().maxPower(s="leetcode") == 2
    assert Solution().maxPower(s="abbcccddddeeeeedcba") == 5
    assert Solution().maxPower(s="triplepillooooow") == 5
    assert Solution().maxPower(s="hooraaaaaaaaaaay") == 11
    assert Solution().maxPower(s="tourist") == 1


if __name__ == '__main__':
    test()
