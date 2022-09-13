#!/usr/bin/env python3
"""
CREATED AT: 2022-09-13

URL: https://leetcode.com/problems/maximum-swap/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 670-MaximumSwap

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Runtime: 53 ms, faster than 33.99%
        Memory Usage: 13.8 MB, less than 70.89%
        0 <= num <= 10^8
        """
        ret = num
        nums = [int(x) for x in str(num)]
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    ret = max(ret, num
                              - nums[i] * 10 ** (n - i - 1)
                              + nums[j] * 10 ** (n - i - 1)
                              - nums[j] * 10 ** (n - j - 1)
                              + nums[i] * 10 ** (n - j - 1)
                              )
            if ret != num:
                return ret
        return ret


def test():
    assert Solution().maximumSwap(num=2736) == 7236
    assert Solution().maximumSwap(num=9973) == 9973


if __name__ == '__main__':
    test()
