#!/usr/bin/env python
"""
CREATED AT: 2021/8/10
Des:

https://leetcode.com/problems/flip-string-to-monotone-increasing/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3876/
GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/flip-string-to-monotone-increasing/solution/
"""
import itertools

from tool import print_results


class Solution:
    @print_results
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        76 / 93 test cases passed.
        Time Limit Exceeded at len(s) = 20000
        :param s:
        :return:
        """

        def __minFMI(s, head: str) -> int:
            if len(s) == 1:
                # last one, no need to flip if head is 0 or s[0] same as head
                if s[0] == head or head == '0':
                    return 0
                else:
                    return 1
            if s[0] == head:
                # head and s[0] are same, no need to flip as we want minimum flips
                return __minFMI(s[1:], head)
            elif head == '0':  # head = 0 and s[0] = 1, has two choices
                # first arg is flip s[0] from 1 to 0, last arg is keep s[0] as 1
                # and head changed to 1
                return min(__minFMI(s[1:], '0') + 1, __minFMI(s[1:], '1'))
            else:
                # head = 1 and s[0] = 0, and must flip s[0] to 1
                return __minFMI(s[1:], '1') + 1

        # assume the virtual head is 0
        return __minFMI(s, '0')

    @print_results
    def minFlipsMonoIncr2(self, s: str) -> int:
        """
        93 / 93 test cases passed.
        Status: Accepted
        Runtime: 372 ms
        Memory Usage: 22.1 MB
        :param s:
        :return:
        """
        l = len(s)

        def add_str(a, b) -> int:
            return int(a) + int(b)

        # break_point_location for break line between s
        # like | 0 | 1 | 0 | 0 |
        # the first one is keep for
        bpl = list(itertools.accumulate(s, func=add_str, initial=0))
        return min([bpl[i] + (l - i - (bpl[-1] - bpl[i])) for i in range(l + 1)])

    @print_results
    def minFlipsMonoIncr3(self, s: str):
        P = [0]
        for x in s:
            P.append(P[-1] + int(x))
        return min(P[j] + len(s) - j - (P[-1] - P[j])
                   for j in range(len(P)))


def test():
    assert Solution().minFlipsMonoIncr(s="0") == 0
    assert Solution().minFlipsMonoIncr(s="1") == 0
    assert Solution().minFlipsMonoIncr(s="00110") == 1
    assert Solution().minFlipsMonoIncr(s="010110") == 2
    assert Solution().minFlipsMonoIncr(s="00011000") == 2

    assert Solution().minFlipsMonoIncr2(s="0") == 0
    assert Solution().minFlipsMonoIncr2(s="1") == 0
    assert Solution().minFlipsMonoIncr2(s="00110") == 1
    assert Solution().minFlipsMonoIncr2(s="010110") == 2
    assert Solution().minFlipsMonoIncr2(s="00011000") == 2

    assert Solution().minFlipsMonoIncr3(s="1") == 0
    assert Solution().minFlipsMonoIncr3(s="0") == 0
    assert Solution().minFlipsMonoIncr3(s="00110") == 1
    assert Solution().minFlipsMonoIncr3(s="010110") == 2
    assert Solution().minFlipsMonoIncr3(s="00011000") == 2


if __name__ == '__main__':
    test()
