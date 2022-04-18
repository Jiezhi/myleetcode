#!/usr/bin/env python
"""
CREATED AT: 2022/4/18
Des:

https://leetcode.com/problems/lexicographical-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        Runtime: 207 ms, faster than 41.64%
        Memory Usage: 19.9 MB, less than 91.92%

        1 <= n <= 5 * 10^4
        """

        def generate(k):
            if k > n:
                return
            yield k
            for i in range(10):
                if k * 10 + i <= n:
                    yield from generate(k * 10 + i)

        ret = []
        for x in range(1, 10):
            ret += list(generate(x))
        return ret


def test():
    assert Solution().lexicalOrder(1) == [1]
    assert Solution().lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    test()
