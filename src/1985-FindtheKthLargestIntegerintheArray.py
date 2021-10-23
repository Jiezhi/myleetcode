#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array
https://leetcode.com/contest/weekly-contest-256/problems/find-the-kth-largest-integer-in-the-array/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(x) for x in nums]
        nums = sorted(nums)
        return str(nums[-k])


def test():
    assert Solution().kthLargestNumber(nums=["3", "6", "7", "10"], k=4) == "3"
    assert Solution().kthLargestNumber(nums=["2", "21", "12", "1"], k=3) == "2"
    assert Solution().kthLargestNumber(nums=["0", "0"], k=2) == "0"


if __name__ == '__main__':
    test()
