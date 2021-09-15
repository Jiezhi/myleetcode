#!/usr/bin/env python
"""
CREATED AT: 2021/9/15
Des:
https://leetcode.com/problems/longest-turbulent-subarray
https://leetcode.com/explore/item/3976
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

"""
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        89 / 89 test cases passed.
        Status: Accepted
        Runtime: 460 ms
        Memory Usage: 18.6 MB
        :param arr:
        :return:
        """
        if len(arr) == 1:
            return 1
        ret = 1
        tmp_ret = 0
        last_flag = None
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                current_flag = None
            else:
                current_flag = arr[i] > arr[i - 1]

            if current_flag is None:
                ret = max(ret, tmp_ret)
                tmp_ret = 1
            elif last_flag is None or last_flag == current_flag:
                ret = max(ret, tmp_ret)
                tmp_ret = 2
            else:
                tmp_ret += 1

            last_flag = current_flag
        return max(ret, tmp_ret)


def test():
    assert Solution().maxTurbulenceSize(arr=[10, 10, 10, 8, 9, 7, 11, 8, 5]) == 6
    assert Solution().maxTurbulenceSize(arr=[9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
    assert Solution().maxTurbulenceSize(arr=[4, 8, 12, 16]) == 2
    assert Solution().maxTurbulenceSize(arr=[100]) == 1
    assert Solution().maxTurbulenceSize(arr=[100, 100]) == 1
    assert Solution().maxTurbulenceSize(arr=[100, 100, 100, 100, 100]) == 1
    assert Solution().maxTurbulenceSize(arr=[101, 100]) == 2
    assert Solution().maxTurbulenceSize(arr=[101, 100, 102]) == 3


if __name__ == '__main__':
    test()
