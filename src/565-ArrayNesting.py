#!/usr/bin/env python
"""
CREATED AT: 2021/9/1
Des:
https://leetcode.com/problems/array-nesting/
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3960/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import random
from timeit import timeit
from typing import List

from tool import print_results


class Solution:
    @print_results
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Analysis when nums = [5,4,0,3,1,6,2], we can found that when the k = range(0, len(nums)):
        k = 0: 5->6->2->0->5, the result is 4
        k = 1: 4->1->4, the result is 2
        k = 2: 0->5->6->2->0, the result is 4
        k = 3: 3->3, the result is 1
        k = 4: 1->4->1, the result is 2
        k = 5: 6->2->0->5->6, the result is 4
        k = 6: 2->0->5->6->2, the result is 4

        Conclusion:
        1. we stop at a circle, and all the number in the circle share the same reslut
        so we can skip the num that in the circle.
        2. all the possibles sum equal to the length of nums,
        so when we get an answer larger than half of the length , that's it!

        856 / 856 test cases passed.
        Status: Accepted
        Runtime: 172 ms
        Memory Usage: 18.4 MB
        :param nums:
        :return:
        """
        ret = 0
        n = len(nums)
        cnted_nums = list()
        for i in range(n):
            num = nums[i]
            if num in cnted_nums:
                continue
            cnted_nums.append(num)
            cnt = 1
            while nums[num] != nums[i]:
                cnt += 1
                num = nums[num]
                cnted_nums.append(num)
            if cnt > (len(nums) // 2):
                return cnt
            ret = max(cnt, ret)
        return ret


def test():
    assert Solution().arrayNesting(nums=[5, 4, 0, 3, 1, 6, 2]) == 4
    assert Solution().arrayNesting(nums=[0, 1, 2]) == 1
    assert Solution().arrayNesting(nums=[0, 2, 1]) == 2
    nums = random.sample(range(10 ** 5), 10 ** 5)

    Solution().arrayNesting(nums=nums)


if __name__ == '__main__':
    test()
