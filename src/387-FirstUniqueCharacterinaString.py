#!/usr/bin/env python
"""
CREATED AT: 2021/8/13
Des:
https://leetcode.com/problems/first-unique-character-in-a-string/
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        104 / 104 test cases passed.
        Status: Accepted
        Runtime: 77 ms
        Memory Usage: 14.6 MB
        :param s:
        :return:
        """
        cnt = collections.Counter(s)
        for k, v in cnt.items():
            if v == 1:
                return s.index(k)
        return -1


def test():
    assert Solution().firstUniqChar(s="leetcode") == 0
    assert Solution().firstUniqChar(s="loveleetcode") == 2
    assert Solution().firstUniqChar(s="aabb") == -1


if __name__ == '__main__':
    test()
