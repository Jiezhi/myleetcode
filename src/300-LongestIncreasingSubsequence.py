#!/usr/bin/env python
"""
CREATED AT: 2022/1/24
Des:
https://leetcode.com/problems/longest-increasing-subsequence/
https://leetcode.com/explore/featured/card/dynamic-programming/632/common-patterns-in-dp-problems/4114/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/
https://leetcode.com/study-plan/dynamic-programming

GITHUB: https://github.com/Jiezhi/myleetcode

Reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
https://en.wikipedia.org/wiki/Patience_sorting
https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)

Difficulty: Medium

Tag:

See:

Time Spent:  min
"""
import bisect
from functools import lru_cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        CREATED AT: 2022/5/25
        Runtime: 118 ms, faster than 80.84%
        Memory Usage: 14.2 MB, less than 48.57%
        1 <= nums.length <= 2500
        -10^4 <= nums[i] <= 10^4
        :param nums:
        :return:
        """
        ret = [nums[0]]

        for num in nums[1:]:
            if num > ret[-1]:
                ret.append(num)
            else:
                pos = bisect.bisect_left(ret, num)
                ret[pos] = num
        return len(ret)

    def lengthOfLIS3(self, nums: List[int]) -> int:
        """
        CREATED AT: 2022/1/24
        Runtime: 4446 ms, faster than 26.80%
        Memory Usage: 14.6 MB, less than 48.56%
        1 <= nums.length <= 2500
        -10^4 <= nums[i] <= 10^4
        :param nums:
        :return:
        """
        # bottom to top
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[x] + 1 if nums[x] < nums[i] else 1 for x in range(i))
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        """
        CREATED AT: 2022/1/24
        54 / 54 test cases passed.
        Status: Accepted
        Runtime: 3652 ms
        Memory Usage: 16.3 MB
        1 <= nums.length <= 2500
        -10^4 <= nums[i] <= 10^4
        :param nums:
        :return:
        """

        # top to bottom
        @lru_cache(None)
        def dp(pos: int) -> int:
            if pos == 0:
                return 1
            return max(dp(x) + 1 if nums[x] < nums[pos] else 1 for x in range(pos))

        return max(dp(x) for x in range(len(nums)))


def test():
    assert Solution().lengthOfLIS(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().lengthOfLIS(nums=[7]) == 1


if __name__ == '__main__':
    test()
