#!/usr/bin/env python3
"""
CREATED AT: 2023-03-09

URL: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2379-MinimumRecolorsToGetKConsecutiveBlackBlocks

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = sum(1 for c in blocks[:k] if c == 'B')
        ret = k - cnt
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'B':
                cnt -= 1
            if blocks[i] == 'B':
                cnt += 1
            ret = min(ret, k - cnt)
            if ret == 0:
                return 0
        return ret


def test():
    assert Solution().minimumRecolors(blocks = "WBBWWBBWBW", k = 7) == 3


if __name__ == '__main__':
    test()

