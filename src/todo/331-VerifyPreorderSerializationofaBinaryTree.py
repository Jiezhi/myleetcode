#!/usr/bin/env python
"""
CREATED AT: 2021/8/26
Des:

https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3920/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pass


def test():
    assert Solution().isValidSerialization(preorder="9,3,4,#,#,1,#,#,2,#,6,#,#")
    assert not Solution().isValidSerialization(preorder="1,#")
    assert not Solution().isValidSerialization(preorder="9,#,#,1")


if __name__ == '__main__':
    test()
