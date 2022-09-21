#!/usr/bin/env python
"""
CREATED AT: 2021/9/9
Des:

https://leetcode.com/problems/jump-game
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from tool import *


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        166 / 166 test cases passed.
        Status: Accepted
        Runtime: 5652 ms
        Memory Usage: 15.3 MB
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return True
        jmp_lst = [False for _ in range(n)]
        jmp_lst[n - 1] = True
        for i in range(n - 2, -1, -1):
            for j in range(min(n - i - 1, nums[i]), 0, -1):
                if jmp_lst[i + j]:
                    jmp_lst[i] = True
                    break
        return jmp_lst[0]

    def canJump2(self, nums: List[int]) -> bool:
        """
        166 / 166 test cases passed.
        Status: Accepted
        Runtime: 500 ms
        Memory Usage: 15.2 MB
        :param nums:
        :return:
        """
        max_step = 0
        for i, n in enumerate(nums):
            if max_step < i:
                return False
            max_step = max(i + n, max_step)
        return True

    def canJump3(self, nums: List[int]) -> bool:
        """
        2022/09/21
        Runtime: 1083 ms, faster than 27.83%
        Memory Usage: 15.2 MB, less than 81.43%

        1 <= nums.length <= 10^4
        0 <= nums[i] <= 10^5
        :param nums:
        :return:
        """
        n = len(nums)
        if n == 1:
            return True
        max_jump = 0
        for i, num in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + num)
            if max_jump >= n - 1:
                return True


def test():
    assert Solution().canJump(nums=[0])
    assert not Solution().canJump(nums=[0, 1])
    assert Solution().canJump(nums=[1, 0])
    assert Solution().canJump(nums=[2, 0, 1])
    assert Solution().canJump(nums=[2, 3, 1, 1, 4])
    assert not Solution().canJump(nums=[3, 2, 1, 0, 4])

    assert Solution().canJump2(nums=[0])
    assert not Solution().canJump2(nums=[0, 1])
    assert Solution().canJump2(nums=[1, 0])
    assert Solution().canJump2(nums=[2, 0, 1])
    assert Solution().canJump2(nums=[2, 3, 1, 1, 4])
    assert not Solution().canJump2(nums=[3, 2, 1, 0, 4])


if __name__ == '__main__':
    test()
