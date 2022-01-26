#!/usr/bin/env python
"""
CREATED AT: 2021/9/28
Solved at: 2022/1/25
Des:
https://leetcode.com/problems/maximum-sum-circular-subarray/
https://leetcode.com/explore/featured/card/dynamic-programming/633/common-patterns-continued/4142/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

See: 53

Ref: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Solved at: 2022/1/26
        111 / 111 test cases passed.
        Status: Accepted
        Runtime: 472 ms, faster than 95.84%
        Memory Usage: 18.4 MB, less than 81.62%
        n == nums.length
        1 <= n <= 3 * 10^4
        -3 * 10^4 <= nums[i] <= 3 * 10^4
        :param nums:
        :return:
        """
        num_sum = tmp_min = max_val = min_val = tmp_max = nums[0]
        for num in nums[1:]:
            num_sum += num
            if tmp_max < 0:
                tmp_max = num
            else:
                tmp_max += num
            max_val = max(max_val, tmp_max)

            if tmp_min > 0:
                tmp_min = num
            else:
                tmp_min += num
            min_val = min(tmp_min, min_val)

        return max(max_val, num_sum - min_val) if num_sum != min_val else max_val


def test():
    assert Solution().maxSubarraySumCircular(nums=[-3, -2, -3]) == -2
    assert Solution().maxSubarraySumCircular(nums=[5, -1, 2, -5, 5]) == 11
    assert Solution().maxSubarraySumCircular(nums=[1, -2, 3, -2]) == 3
    assert Solution().maxSubarraySumCircular(nums=[5, -3, 5]) == 10
    assert Solution().maxSubarraySumCircular(nums=[3, -1, 2, -1]) == 4
    assert Solution().maxSubarraySumCircular(nums=[3, 1, 2, -1, 4]) == 10


if __name__ == '__main__':
    test()
