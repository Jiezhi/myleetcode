#!/usr/bin/env python3
"""
CREATED AT: 2022-10-09

URL: https://leetcode.com/contest/weekly-contest-314/problems/find-the-original-array-of-prefix-xor/
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2433-FindTheOriginalArrayOfPrefixXor

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        1 <= pref.length <= 10^5
        0 <= pref[i] <= 10^6
        """
        ret = [0] * len(pref)
        ret[0] = pref[0]
        pre = ret[0]
        for i, v in enumerate(pref[1:], 1):
            ret[i] = pre ^ pref[i]
            pre ^= ret[i]
        return ret


def test():
    assert Solution().findArray(pref=[5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]
    assert Solution().findArray(pref=[13]) == [13]


if __name__ == '__main__':
    test()
