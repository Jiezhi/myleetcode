#!/usr/bin/env python3
"""
CREATED AT: 2022-09-21

URL: https://leetcode.com/problems/sum-of-even-numbers-after-queries/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 985-SumOfEvenNumbersAfterQueries

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Runtime: 1231 ms, faster than 14.54%
        Memory Usage: 20.5 MB, less than 43.88%

        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        1 <= queries.length <= 10^4
        -10^4 <= vali <= 10^4
        0 <= indexi < nums.length
        """
        ret = []
        even_sum = sum(x for x in nums if x & 1 == 0)
        for val, pos in queries:
            if nums[pos] & 1 == 0:
                if val & 1 == 0:
                    even_sum += val
                else:
                    even_sum -= nums[pos]
            elif val & 1:
                even_sum += nums[pos] + val
            nums[pos] += val
            ret.append(even_sum)
        return ret


def test():
    assert Solution().sumEvenAfterQueries(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]) == [8, 6, 2, 4]
    assert Solution().sumEvenAfterQueries(nums=[1], queries=[[4, 0]]) == [0]


if __name__ == '__main__':
    test()
