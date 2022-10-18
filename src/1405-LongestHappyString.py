#!/usr/bin/env python
"""
CREATED AT: 2021/12/29
Des:

https://leetcode.com/problems/longest-happy-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag:

See:

Time Spent:  min
"""
from tool import *


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Runtime: 75 ms, faster than 5.73%
        Memory Usage: 13.9 MB, less than 90.28%

        0 <= a, b, c <= 100
        a + b + c > 0
        """
        cnt = collections.Counter()
        if a > 0:
            cnt['a'] = a
        if b > 0:
            cnt['b'] = b
        if c > 0:
            cnt['c'] = c
        ret = []
        while len(cnt) > 1:
            (max1, _), (max2, _) = cnt.most_common(2)
            if len(ret) > 1 and ret[-1] == max1 and ret[-2] == max1:
                ret.append(max2)
                cnt[max2] -= 1
                if not cnt[max2]:
                    del cnt[max2]
            else:
                ret.append(max1)
                cnt[max1] -= 1
                if not cnt[max1]:
                    del cnt[max1]
        if cnt:
            k, v = cnt.most_common(1)[0]
            if v >= 2:
                ret.append(k)
                ret.append(k)
            else:
                ret.append(k)
        return ''.join(ret)


def test():
    assert Solution().longestDiverseString(a=1, b=1, c=7) in ["ccaccbcc", "ccbccacc"]
    assert Solution().longestDiverseString(a=7, b=1, c=0) in ["aabaa"]


if __name__ == '__main__':
    test()
