#!/usr/bin/env python
"""
CREATED AT: 2021/8/18
Des:
https://leetcode.com/problems/decode-ways/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3902/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from functools import lru_cache

from tool import print_results


class Solution:
    @print_results
    def numDecodings(self, s: str) -> int:
        """
        269 / 269 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.6 MB
        :param s:
        :return:
        """

        @lru_cache(None)
        def dp(i):
            # reach the end, the solution is ok
            if i == len(s):
                return 1
            # encounter a zero at the head, the solution is invalid.
            if s[i] == '0':
                return 0
            ans = dp(i + 1)
            if i + 1 < len(s) and int(s[i:i + 2]) < 27:
                ans += dp(i + 2)
            return ans

        return dp(0)


def test():
    assert Solution().numDecodings(s="12") == 2
    assert Solution().numDecodings(s="11106") == 2
    assert Solution().numDecodings(s="226") == 3
    assert Solution().numDecodings(s="0") == 0
    assert Solution().numDecodings(s="06") == 0


if __name__ == '__main__':
    test()
