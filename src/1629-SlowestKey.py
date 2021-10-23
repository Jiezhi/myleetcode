#!/usr/bin/env python
"""
CREATED AT: 2021/9/6
Des:
https://leetcode.com/problems/slowest-key
https://leetcode.com/explore/item/3965
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        105 / 105 test cases passed.
        Status: Accepted
        Runtime: 48 ms
        Memory Usage: 14.3 MB
        :param releaseTimes:
        :param keysPressed:
        :return:
        """
        tmp_max = releaseTimes[0]
        ret = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            t = releaseTimes[i] - releaseTimes[i - 1]
            if t > tmp_max:
                tmp_max = t
                ret = keysPressed[i]
            if t == tmp_max:
                ret = max(ret, keysPressed[i])
        return ret


def test():
    assert Solution().slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd") == 'c'
    assert Solution().slowestKey(releaseTimes=[50, 9, 29, 49, 50], keysPressed="zcbcd") == 'z'
    assert Solution().slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda") == 'a'


if __name__ == '__main__':
    test()
