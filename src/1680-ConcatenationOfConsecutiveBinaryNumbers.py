#!/usr/bin/env python3
"""
CREATED AT: 2022-09-23

URL: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1680-ConcatenationOfConsecutiveBinaryNumbers

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/solution/lian-jie-lian-xu-er-jin-zhi-shu-zi-by-ze-t40j/

"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Runtime: 2060 ms, faster than 66.93%
        Memory Usage: 13.9 MB, less than 80.31%

        1 <= n <= 10^5
        """
        module = 10 ** 9 + 7
        ret, shift = 0, 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                shift += 1
            ret = ((ret << shift) + i) % module
        return ret


def test():
    assert Solution().concatenatedBinary(n=1) == 1
    assert Solution().concatenatedBinary(n=3) == 27
    assert Solution().concatenatedBinary(n=12) == 505379714


if __name__ == '__main__':
    test()
