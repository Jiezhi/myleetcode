#!/usr/bin/env python
"""
CREATED AT: 2022/3/27
Des:
https://leetcode.com/problems/find-palindrome-with-fixed-length/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""

from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        1 <= queries.length <= 5 * 10^4
        1 <= queries[i] <= 10^9
        1 <= intLength <= 15
        """

        def build(q) -> int:
            l = [0] * intLength
            l[0] = 1
            q -= 1
            pos = (intLength + 1) // 2 - 1
            while q != 0:
                q, left = divmod(q, 10)
                l[pos] += left
                pos -= 1
            lo, hi = 0, len(l) - 1
            while lo < hi:
                l[hi] = l[lo]
                lo += 1
                hi -= 1
            k = 1
            ret = 0
            pos = len(l) - 1
            while pos >= 0:
                ret += l[pos] * k
                k *= 10
                pos -= 1
            return ret

        if intLength == 1:
            return [x if 0 < x < 10 else -1 for x in queries]
        else:
            max_q = 9 * 10 ** ((intLength + 1) // 2 - 1)

        ret = [-1] * len(queries)
        for i, q in enumerate(queries):
            if q <= max_q:
                ret[i] = build(q)

        return ret


def test():
    assert Solution().kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3) == [101, 111, 121, 131, 141, 999]
    assert Solution().kthPalindrome(queries=[2, 4, 6], intLength=4) == [1111, 1331, 1551]


if __name__ == '__main__':
    test()
