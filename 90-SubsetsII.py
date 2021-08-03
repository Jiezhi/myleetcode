#!/usr/bin/env python
"""
CREATED AT: 2021/8/3
Des:

https://leetcode.com/problems/subsets-ii/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3837/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            tmp_ret = ret.copy()
            for sub in tmp_ret:
                s = sub.copy()
                s.append(n)
                # [1, 4] and [4, 1] are same in this problem, so sort to avoid.
                if s:
                    s = sorted(s)
                if s not in ret:
                    ret.append(s)
        return ret


def test():
    # 这题是我没理解清楚还是本身就有歧义，按这个答案来讲，[1, 4]和[4, 1]是重复的
    answer = [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
    ret = Solution().subsetsWithDup(nums=[4, 4, 4, 1, 4])
    assert len(answer) == len(ret)
    for a in answer:
        assert a in ret

    answer = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    ret = Solution().subsetsWithDup(nums=[1, 2, 3])
    assert len(answer) == len(ret)
    for a in answer:
        assert a in ret

    answer = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    ret = Solution().subsetsWithDup(nums=[1, 2, 2])
    assert len(answer) == len(ret)
    for a in answer:
        assert a in ret

    answer = [[], [2]]
    ret = Solution().subsetsWithDup(nums=[2])
    assert len(answer) == len(ret)
    for a in answer:
        assert a in ret


if __name__ == '__main__':
    test()
