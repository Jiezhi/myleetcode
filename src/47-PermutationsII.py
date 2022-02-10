#!/usr/bin/env python
"""
CREATED AT: 2021/10/27
Des:

https://leetcode.com/problems/permutations-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        CREATED AT: 2022/2/10
        Same as 46, but remove duplicates  list[list] -> list[str]->set->list
        Runtime: 103 ms, faster than 38.36%
        Memory Usage: 14.4 MB, less than 81.59%
        1 <= nums.length <= 8
        -10 <= nums[i] <= 10
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return [nums]

        dp = self.permuteUnique(nums[:-1])
        ret = []

        for d in dp:
            for i in range(len(d) + 1):
                dcopy = d.copy()
                dcopy.insert(i, nums[-1])
                ret.append(dcopy)
        ret_set = set(str(x) for x in ret)
        ret = []
        for r in ret_set:
            tmp_ret = []
            for c in r.replace('[', '').replace(']', '').replace(',', '').split():
                tmp_ret.append(int(c))
            ret.append(tmp_ret)
        return ret


def test():
    ans = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    ret = Solution().permuteUnique(nums=[1, 1, 2])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret

    ans = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    ret = Solution().permuteUnique(nums=[1, 2, 3])
    assert len(ans) == len(ret)
    for a in ans:
        assert a in ret


if __name__ == '__main__':
    test()
