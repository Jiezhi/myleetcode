#!/usr/bin/env python3
"""
CREATED AT: 2022-10-23

URL: https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2449-MinimumNumberOfOperationsToMakeArraysSimilar

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        """
        Runtime: 1406 ms, faster than 75.00%
        Memory Usage: 43.1 MB, less than 8.33%
        
        n == nums.length == target.length
        1 <= n <= 10^5
        1 <= nums[i], target[i] <= 10^6
        It is possible to make nums similar to target.
        """
        source_cnt, target_cnt = Counter(nums), Counter(target)
        if source_cnt == target_cnt:
            return 0
        ret = 0
        source_list, target_list = sorted(source_cnt.keys()), sorted(target_cnt, reverse=True)
        odd, even = [], []
        for num in source_list:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)

        del source_list

        for tnum in target_list:
            while target_cnt[tnum]:
                if tnum & 1:
                    snum = odd[-1]
                    cur = odd
                else:
                    snum = even[-1]
                    cur = even
                if target_cnt[tnum] >= source_cnt[snum]:
                    target_cnt[tnum] -= source_cnt[snum]
                    ret += abs(tnum - snum) * source_cnt[snum]
                    del source_cnt[snum]
                    cur.pop()
                else:
                    source_cnt[snum] -= target_cnt[tnum]
                    ret += abs(tnum - snum) * target_cnt[tnum]
                    del target_cnt[tnum]
        return ret // 4


def test():
    assert Solution().makeSimilar(nums=[8, 12, 6], target=[2, 14, 10]) == 2
    assert Solution().makeSimilar(nums=[1, 2, 5], target=[4, 1, 3]) == 1
    assert Solution().makeSimilar(nums=[1, 1, 1, 1, 1], target=[1, 1, 1, 1, 1]) == 0


if __name__ == '__main__':
    test()
