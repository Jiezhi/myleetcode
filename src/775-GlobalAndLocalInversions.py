#!/usr/bin/env python3
"""
CREATED AT: 2022-11-16

URL: https://leetcode.com/problems/global-and-local-inversions/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 775-GlobalAndLocalInversions

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.cn/problems/global-and-local-inversions/solution/quan-ju-dao-zhi-yu-ju-bu-dao-zhi-by-leet-bmjp/
https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution

"""
from tool import *


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        """
        TLE on LC
        n == nums.length
        1 <= n <= 10^5
        0 <= nums[i] < n
        All the integers of nums are unique.
        nums is a permutation of all the numbers in the range [0, n - 1].
        """
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))


def test():
    assert Solution().isIdealPermutation(nums=[1, 0, 2])
    assert not Solution().isIdealPermutation(nums=[1, 2, 0])


if __name__ == '__main__':
    test()
