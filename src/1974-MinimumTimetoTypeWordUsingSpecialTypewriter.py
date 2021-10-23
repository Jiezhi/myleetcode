#!/usr/bin/env python
"""
CREATED AT: 2021/8/21
Des:

https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter
https://leetcode.com/contest/biweekly-contest-59/problems/minimum-time-to-type-word-using-special-typewriter/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from tool import print_results


class Solution:
    @print_results
    def minTimeToType(self, word: str) -> int:
        current = 'a'
        steps = 0
        for w in word:
            diff = abs(ord(current) - ord(w))
            if diff > 13:
                diff = 26 - diff
            steps += diff + 1
            current = w
        return steps


def test():
    assert Solution().minTimeToType(word="abc") == 5
    assert Solution().minTimeToType(word="bza") == 7
    assert Solution().minTimeToType(word="zjpc") == 34


if __name__ == '__main__':
    test()
