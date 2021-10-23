#!/usr/bin/env python
"""
CREATED AT: 2021/9/5
Des:
https://leetcode.com/problems/subsets/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        10 / 10 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.2 MB
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return [[], [nums[0]]]
        last_ret = self.subsets(nums[:-1])
        ret = []
        for r in last_ret:
            tmp_r = r.copy()
            tmp_r.append(nums[-1])
            ret.append(r)
            ret.append(tmp_r)
        return ret


def test():
    ans = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    ret = Solution().subsets(nums=[1, 2, 3])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    ans = [[], [1]]
    ret = Solution().subsets(nums=[1])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
