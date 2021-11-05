#!/usr/bin/env python
"""
CREATED AT: 2021/10/30
Des:

https://leetcode.com/problems/kth-distinct-string-in-an-array/
https://leetcode.com/contest/biweekly-contest-64/problems/kth-distinct-string-in-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        1 <= k <= arr.length <= 1000
        1 <= arr[i].length <= 5
        arr[i] consists of lowercase English letters.
        :param arr:
        :param k:
        :return:
        """
        cnt = 1
        duplicateStr = set()
        for i in range(len(arr)):
            if arr[i] in duplicateStr:
                continue
            if i < len(arr) - 1 and arr[i] in arr[i + 1:]:
                duplicateStr.add(arr[i])
            else:
                if cnt == k:
                    return arr[i]
                else:
                    cnt += 1
        return ""


def test():
    assert Solution().kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2) == "a"
    assert Solution().kthDistinct(arr=["aaa", "aa", "a"], k=1) == "aaa"
    assert Solution().kthDistinct(arr=["a", "b", "a"], k=3) == ""


if __name__ == '__main__':
    test()
