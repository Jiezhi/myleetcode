#!/usr/bin/env python
"""
CREATED AT: 2021/9/6
Des:
https://leetcode.com/problems/top-k-frequent-elements/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium


TODO: do with [Quickselect](https://www.wikiwand.com/en/Quickselect)
"""
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        21 / 21 test cases passed.
        Status: Accepted
        Runtime: 100 ms
        Memory Usage: 18.8 MB
        :param nums:
        :param k:
        :return:
        """
        ret = collections.Counter(nums).most_common(k)
        return [x[0] for x in ret]


def test():
    assert Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2) == [1, 2]
    assert Solution().topKFrequent(nums=[1], k=1) == [1]


if __name__ == '__main__':
    test()
