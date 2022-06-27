#!/usr/bin/env python3
"""
CREATED AT: 2022-06-27

URL: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1689-PartitioningIntoMinimumNumberOfDeci-BinaryNumbers

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Runtime: 69 ms, faster than 89.63%
        Memory Usage: 14.7 MB, less than 83.73%
        1 <= n.length <= 10^5
        n consists of only digits.
        n does not contain any leading zeros and represents a positive integer.
        """

        return int(max(n))


def test():
    assert Solution().minPartitions(n="32") == 3
    assert Solution().minPartitions(n="82734") == 8
    assert Solution().minPartitions(n="27346209830709182346") == 9


if __name__ == '__main__':
    test()
