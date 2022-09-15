#!/usr/bin/env python3
"""
CREATED AT: 2022-09-15

URL: https://leetcode.com/problems/find-original-array-from-doubled-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2007-FindOriginalArrayFromDoubledArray

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        Runtime: 3316 ms, faster than 13.04%
        Memory Usage: 32.1 MB, less than 70.28%

        1 <= changed.length <= 10^5
        0 <= changed[i] <= 10^5
        """
        n = len(changed)
        if (n & 1) == 1:
            return []
        cnt = Counter(changed)
        ret = []
        if 0 in cnt:
            if (cnt[0] & 1) == 0:
                ret += [0] * (cnt[0] // 2)
            else:
                return []
        for num in sorted(cnt.keys()):
            if num == 0 or cnt[num] == 0:
                continue
            if num * 2 not in cnt or cnt[num * 2] < cnt[num]:
                return []
            ret += [num] * cnt[num]
            cnt[num * 2] -= cnt[num]
        return ret


def test():
    assert Solution().findOriginalArray(changed=[0, 0, 0, 0]) == [0, 0]
    assert Solution().findOriginalArray(changed=[0, 0, 0, 0, 0]) == []
    assert Solution().findOriginalArray(changed=[1, 3, 4, 2, 6, 8]) == [1, 3, 4]
    assert Solution().findOriginalArray(changed=[6, 3, 0, 1]) == []
    assert Solution().findOriginalArray(changed=[1]) == []


if __name__ == '__main__':
    test()
