#!/usr/bin/env python3
"""
CREATED AT: 2022-10-15

URL: https://leetcode.com/problems/build-an-array-with-stack-operations/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1441-BuildAnArrayWithStackOperations

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        Runtime: 37 ms, faster than 89.34%
        Memory Usage: 13.8 MB, less than 68.53%

        1 <= target.length <= 100
        1 <= n <= 100
        1 <= target[i] <= n
        target is strictly increasing.
        """
        num, i = 1, 0
        ret = []
        while target[-1] >= num:
            while target[i] > num:
                ret.append('Push')
                ret.append('Pop')
                num += 1
            ret.append('Push')
            num += 1
            i += 1
        return ret


def test():
    assert Solution().buildArray(target=[1, 3], n=3) == ["Push", "Push", "Pop", "Push"]
    assert Solution().buildArray(target=[1, 2, 3], n=3) == ["Push", "Push", "Push"]
    assert Solution().buildArray(target=[1, 2], n=4) == ["Push", "Push"]


if __name__ == '__main__':
    test()
