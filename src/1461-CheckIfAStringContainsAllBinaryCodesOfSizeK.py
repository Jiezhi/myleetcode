#!/usr/bin/env python
"""
CREATED AT: 2022/5/31
Des:
https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Runtime: 349 ms, faster than 90.71%
        Memory Usage: 27.2 MB, less than 51.77%
        1 <= s.length <= 5 * 10^5
        s[i] is either '0' or '1'.
        1 <= k <= 20
        :param s:
        :param k:
        :return:
        """
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k


def test():
    assert Solution().hasAllCodes("00110110", 2)
    assert Solution().hasAllCodes("00110", 2)


if __name__ == '__main__':
    test()
