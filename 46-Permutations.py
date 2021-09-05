#!/usr/bin/env python
"""
CREATED AT: 2021/9/5
Des:

https://leetcode.com/problems/permutations/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        26 / 26 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.5 MB
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return [nums]
        pre_ret = self.permute(nums[1:])
        ret = []
        for r in pre_ret:
            for i in range(len(r) + 1):
                tmp_r = r.copy()
                tmp_r.insert(i, nums[0])
                ret.append(tmp_r)
        return ret


def test():
    ans = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    ret = Solution().permute([1, 2, 3])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    ans = [[0, 1], [1, 0]]
    ret = Solution().permute(nums=[0, 1])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    assert Solution().permute(nums=[1]) == [[1]]


if __name__ == '__main__':
    test()
