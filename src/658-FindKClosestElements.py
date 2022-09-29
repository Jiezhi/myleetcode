#!/usr/bin/env python
"""
CREATED AT: 2021/12/23
Des:

https://leetcode.com/problems/find-k-closest-elements/
https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: BS

See:

Ref: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)

"""
from tool import *


class Solution:
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Runtime: 847 ms, faster than 12.34%
        Memory Usage: 15.4 MB, less than 80.93%
        1 <= k <= arr.length
        1 <= arr.length <= 10^4
        arr is sorted in ascending order.
        -10^4 <= arr[i], x <= 10^4
        """
        i = bisect.bisect_left(arr, x) - 1
        ret = []
        j = i + 1
        while len(ret) < k and i >= 0 and j < len(arr):
            a, b = abs(arr[i] - x), abs(arr[j] - x)
            if a == b or a < b:
                ret.append(arr[i])
                i -= 1
            else:
                ret.append(arr[j])
                j += 1
        if len(ret) < k:
            while len(ret) < k and i >= 0:
                ret.append(arr[i])
                i -= 1
            while len(ret) < k and j < len(arr):
                ret.append(arr[j])
                j += 1
        return sorted(ret)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        63 / 63 test cases passed.
        Status: Accepted
        Runtime: 280 ms
        Memory Usage: 15.4 MB
        1 <= k <= arr.length
        1 <= arr.length <= 10^4
        arr is sorted in ascending order.
        -10^4 <= arr[i], x <= 10^4
        """
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low + high) // 2
            if (x - arr[mid]) > (arr[mid + k] - x):
                low = mid + 1
            else:
                high = mid
        return arr[low:low + k]


def test():
    assert Solution().findClosestElements(arr=[1, 2, 5, 5, 6, 6, 7, 7, 8, 9], k=7, x=7) == [5, 5, 6, 6, 7, 7, 8]
    assert Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=2, x=3) == [2, 3]
    assert Solution().findClosestElements(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3, x=1) == [1, 2, 3]
    assert Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3) == [1, 2, 3, 4]
    assert Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1) == [1, 2, 3, 4]


if __name__ == '__main__':
    test()
