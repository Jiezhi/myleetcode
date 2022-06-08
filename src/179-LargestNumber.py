#!/usr/bin/env python3
"""
CREATED AT: 2022-06-08
Des: https://leetcode.com/problems/largest-number/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty:  Medium

Tag: 

See: 

"""
import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Runtime: 77 ms, faster than 26.45%
        Memory Usage: 13.8 MB, less than 67.07%
        1 <= nums.length <= 100
        0 <= nums[i] <= 10^9
        """

        def get_list(n: int) -> List[int]:
            if n == 0:
                return [0]
            ret = []
            while n > 0:
                ret.append(n % 10)
                n //= 10
            return ret

        def compare(x: int, y: int) -> int:
            lx = get_list(x)
            ly = get_list(y)
            lx, ly = lx[::-1], ly[::-1]
            lx, ly = lx + ly, ly + lx
            i = 0
            while i < len(lx):
                if lx[i] > ly[i]:
                    return 1
                elif lx[i] < ly[i]:
                    return -1
                i += 1
            return 0

        nums = sorted(nums, key=functools.cmp_to_key(compare), reverse=True)
        print(nums)
        if nums[0] == 0:
            return '0'
        return ''.join(str(x) for x in nums)

    def largestNumber2(self, nums: List[int]) -> str:
        """
        Runtime: 44 ms, faster than 82.75%
        Memory Usage: 13.8 MB, less than 67.07%
        1 <= nums.length <= 100
        0 <= nums[i] <= 10^9
        """

        def compare(x: str, y: str) -> int:
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0

        ret = ''.join(sorted(map(str, nums), key=functools.cmp_to_key(compare), reverse=True))
        return ret if ret[0] != '0' else '0'


def test():
    inputs = [[32, 323], [32, 322], [10, 2], [3, 30, 34, 5, 9], [111311, 1113]]
    answers = ['32332', '32322', '210', '9534330', "1113111311"]
    assert list(map(Solution().largestNumber, inputs)) == answers
    assert list(map(Solution().largestNumber2, inputs)) == answers


if __name__ == '__main__':
    test()
