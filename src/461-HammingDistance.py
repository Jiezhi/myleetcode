#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/hamming-distance/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/99/others/762/
GITHUB: https://github.com/Jiezhi/myleetcode

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        149 / 149 test cases passed.
        Runtime: 32 ms, faster than 62.28%
        Memory Usage: 14.3 MB, less than 44.82%
        :param x:
        :param y:
        :return:
        """
        # '0b100' remove '0b'
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        # make sure x_bin be the longest str
        if len(x_bin) < len(y_bin):
            x_bin, y_bin = y_bin, x_bin
        distance = 0
        for i in range(1, len(y_bin) + 1):
            if x_bin[-i] != y_bin[-i]:
                distance += 1
        for i in range(len(x_bin) - len(y_bin)):
            if x_bin[i] == '1':
                distance += 1
        return distance


def test():
    assert Solution().hammingDistance(x=1, y=4) == 2
    assert Solution().hammingDistance(x=3, y=1) == 1


if __name__ == '__main__':
    test()
