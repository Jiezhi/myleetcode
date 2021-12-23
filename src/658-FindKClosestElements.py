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
from typing import List


class Solution:
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
        :param arr:
        :param k:
        :param x:
        :return:
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
