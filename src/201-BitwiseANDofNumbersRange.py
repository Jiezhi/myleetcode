#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:
https://leetcode.com/problems/bitwise-and-of-numbers-range/
GITHUB: https://github.com/Jiezhi/myleetcode
Reference: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56721/2-line-Solution(the-fastest)-with-detailed-explanation
Difficulty: Medium
Tags: Bit Manipulation
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Runtime: 52 ms, faster than 91.55% of Python3 online submissions for Bitwise AND of Numbers Range.
        Memory Usage: 14.3 MB, less than 23.30% of Python3 online submissions for Bitwise AND of Numbers Range.
        :param left:
        :param right:
        :return:
        """
        while left < right:
            right = right & (right - 1)
        return right


def test():
    assert Solution().rangeBitwiseAnd(left=5, right=7) == 4
    assert Solution().rangeBitwiseAnd(left=0, right=0) == 0
    assert Solution().rangeBitwiseAnd(left=1, right=2147483647) == 0


if __name__ == '__main__':
    test()
