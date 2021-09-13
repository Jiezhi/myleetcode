#!/usr/bin/env python
"""
CREATED AT: 2021/9/13
Des:
https://leetcode.com/problems/maximum-number-of-balloons
https://leetcode.com/explore/item/3973
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        24 / 24 test cases passed.
        Status: Accepted
        Runtime: 28 ms
        Memory Usage: 14.5 MB

        balloon
        :param text:
        :return:
        """
        cnt = collections.Counter(text)
        return min(cnt['b'], cnt['a'], cnt['l'] // 2, cnt['o'] // 2, cnt['n'])


def test():
    assert Solution().maxNumberOfBalloons(text="nlaebolko") == 1
    assert Solution().maxNumberOfBalloons(text="loonbalxballpoon") == 2
    assert Solution().maxNumberOfBalloons(text="leetcode") == 0


if __name__ == '__main__':
    test()
