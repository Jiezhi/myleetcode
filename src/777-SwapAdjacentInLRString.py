#!/usr/bin/env python3
"""
CREATED AT: 2022-10-02

URL: https://leetcode.com/problems/swap-adjacent-in-lr-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 777-SwapAdjacentInLRString

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.cn/problems/swap-adjacent-in-lr-string/solution/zai-lrzi-fu-chuan-zhong-jiao-huan-xiang-rjaw8/

"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        Runtime: 85 ms, faster than 54.13%
        Memory Usage: 13.9 MB, less than 98.74%

        1 <= start.length <= 10^4
        start.length == end.length
        Both start and end will only consist of characters in 'L', 'R', and 'X'.
        a move consists of either replacing one occurrence of "XL" with "LX",
        or replacing one occurrence of "RX" with "XR"
        """
        i, j, n = 0, 0, len(start)
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1

            while j < n and end[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                if start[i] == 'L' and i < j:
                    return False
                if start[i] == 'R' and i > j:
                    return False
                i += 1
                j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1

        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True


def test():
    assert Solution().canTransform(start="RXXLRXRXL", end="XRLXXRRLX")
    assert not Solution().canTransform(start="X", end="L")


if __name__ == '__main__':
    test()
