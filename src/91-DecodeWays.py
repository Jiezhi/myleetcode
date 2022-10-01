#!/usr/bin/env python3
"""
CREATED AT: 2022-10-01

URL: https://leetcode.com/problems/decode-ways/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3902/
GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 91-DecodeWays

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    @print_results
    def numDecodings(self, s: str) -> int:
        """
        2021/8/18
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

    def numDecodings2(self, s: str) -> int:
        """
        2022-10-01
        Runtime: 37 ms, faster than 87.73%
        Memory Usage: 14.5 MB, less than 7.07%

        1 <= s.length <= 100
        s contains only digits and may contain leading zero(s).
        """
        valid_two = {str(x) for x in range(10, 27)}

        @cache
        def dp(s: str) -> int:
            if not s:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            ret = dp(s[1:])
            if s[:2] in valid_two:
                ret += dp(s[2:])
            return ret

        return dp(s)


def test():
    assert Solution().numDecodings(s="12") == 2
    assert Solution().numDecodings(s="11106") == 2
    assert Solution().numDecodings(s="226") == 3
    assert Solution().numDecodings(s="0") == 0
    assert Solution().numDecodings(s="06") == 0


if __name__ == '__main__':
    test()
