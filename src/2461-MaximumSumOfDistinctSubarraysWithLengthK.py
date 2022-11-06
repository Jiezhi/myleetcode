#!/usr/bin/env python3
"""
CREATED AT: 2022-11-06

URL: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
https://leetcode.com/contest/weekly-contest-318/problems/maximum-sum-of-distinct-subarrays-with-length-k/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2461-MaximumSumOfDistinctSubarraysWithLengthK

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        1 <= k <= nums.length <= 10^5
        1 <= nums[i] <= 10^5
        """
        cnt = Counter(nums[:k])
        s = sum(nums[:k])
        ret = 0 if len(cnt) < k else s
        for i in range(k, len(nums)):
            cnt[nums[i]] += 1
            if cnt[nums[i - k]] == 1:
                del cnt[nums[i - k]]
            else:
                cnt[nums[i - k]] -= 1
            s += nums[i] - nums[i - k]
            if len(cnt) == k and s > ret:
                ret = s
        return ret


def test():
    assert Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15
    assert Solution().maximumSubarraySum(nums=[4, 4, 4], k=3) == 0


if __name__ == '__main__':
    test()
