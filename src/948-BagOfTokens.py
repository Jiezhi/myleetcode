#!/usr/bin/env python3
"""
CREATED AT: 2022-09-12

URL: https://leetcode.com/problems/bag-of-tokens/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 948-BagOfTokens

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        Runtime: 53 ms, faster than 97.64%
        Memory Usage: 14.1 MB, less than 7.08%

        0 <= tokens.length <= 1000
        0 <= tokens[i], power < 10^4
        """
        tokens.sort()
        l, r = 0, len(tokens) - 1
        ret, tmp_ret = 0, 0
        while l <= r:
            while l <= r and power >= tokens[l]:
                power -= tokens[l]
                tmp_ret += 1
                l += 1
            ret = max(ret, tmp_ret)
            if l <= r:
                if tmp_ret > 0:
                    tmp_ret -= 1
                    power += tokens[r]
                    r -= 1
                else:
                    break
        return ret


def test():
    assert Solution().bagOfTokensScore(tokens=[50, 50, 50, 100, 100], power=50) == 2
    assert Solution().bagOfTokensScore(tokens=[50], power=50) == 1
    assert Solution().bagOfTokensScore(tokens=[100], power=50) == 0
    assert Solution().bagOfTokensScore(tokens=[100, 200], power=150) == 1
    assert Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], power=200) == 2


if __name__ == '__main__':
    test()
