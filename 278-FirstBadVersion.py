#!/usr/bin/env python
"""
CREATED AT: 2021/8/22
Des:

https://leetcode.com/problems/first-bad-version/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/774/

GITHUB: https://github.com/Jiezhi/myleetcode

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
bad = 0
called_cnt = 0


def isBadVersion(version):
    global called_cnt
    called_cnt += 1
    return version >= bad


class Solution:
    def firstBadVersion(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


def test():
    global bad, called_cnt
    called_cnt, bad = 0, 4
    assert Solution().firstBadVersion(n=5) == bad
    assert called_cnt == 2
    called_cnt, bad = 0, 1
    assert Solution().firstBadVersion(n=1) == bad
    assert called_cnt == 0


if __name__ == '__main__':
    test()
