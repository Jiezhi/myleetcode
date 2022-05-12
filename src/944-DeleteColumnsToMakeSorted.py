#!/usr/bin/env python
"""
CREATED AT: 2022/5/12
Des:
https://leetcode.com/problems/delete-columns-to-make-sorted/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Runtime: 198 ms, faster than 57.99%
        Memory Usage: 14.8 MB, less than 31.41%
        n == strs.length
        1 <= n <= 100
        1 <= strs[i].length <= 1000
        strs[i] consists of lowercase English letters.
        :param strs:
        :return:
        """
        l = len(strs[0])
        ret = 0
        for i in range(l):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    ret += 1
                    break
        return ret


def test():
    assert Solution().minDeletionSize(["cba", "daf", "ghi"]) == 1


if __name__ == '__main__':
    test()
