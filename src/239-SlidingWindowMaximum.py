#!/usr/bin/env python
"""
CREATED AT: 2021/11/16
Des:

https://leetcode.com/problems/sliding-window-maximum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/hua-dong-chuang-kou-de-zui-da-zhi-by-lee-ymyo/
"""
import collections
import heapq
from typing import List


class Solution:
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
        Use python heapq
        Runtime: 1976 ms, faster than 43.70%
        Memory Usage: 39 MB, less than 5.23%
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        1 <= k <= nums.length
        :param nums:
        :param k:
        :return:
        """
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ret = [-q[0][0]]
        for i in range(k, len(nums)):
            while q and q[0][1] <= i - k:
                heapq.heappop(q)
            heapq.heappush(q, (-nums[i], i))
            ret.append(-q[0][0])

        return ret

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: 1876 ms, faster than 50.69%
        Memory Usage: 30.1 MB, less than 55.84%
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        1 <= k <= nums.length
        :param nums:
        :param k:
        :return:
        """
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        def maintain_dq(dq, index):
            while len(dq) > 0 and dq[-1][0] <= nums[index]:
                dq.pop()
            dq.append((nums[index], index))

        # save num and its index tuple
        dq = collections.deque()
        dq.append((nums[0], 0))
        for i in range(1, k):
            maintain_dq(dq, i)
        ret = [dq[0][0]]
        for i in range(k, len(nums)):
            if i - dq[0][1] >= k:
                dq.popleft()
            maintain_dq(dq, i)
            ret.append(dq[0][0])
        return ret


def test():
    with open('239-testcase.txt') as f:
        nums = f.readline()
        nums = nums.strip('[]\n').split(',')
        nums = [int(x) for x in nums]
        k = int(f.readline())
        assert Solution().maxSlidingWindow(nums=nums, k=k) == Solution().maxSlidingWindow2(nums=nums, k=k)
    assert Solution().maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3) == [3, 3, 2, 5]
    assert Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert Solution().maxSlidingWindow(nums=[1], k=1) == [1]
    assert Solution().maxSlidingWindow(nums=[9, 11], k=2) == [11]


if __name__ == '__main__':
    test()
