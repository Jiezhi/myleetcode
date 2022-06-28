#!/usr/bin/env python3
"""
CREATED AT: 2022-06-28

URL: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1647-MinimumDeletionsToMakeCharacterFrequenciesUnique

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Runtime: 185 ms, faster than 71.62% 
        Memory Usage: 14.8 MB, less than 51.90% 

        1 <= s.length <= 10^5
        s contains only lowercase English letters.
        """
        cnt = collections.Counter(s)

        nums = collections.defaultdict(int)
        for k, v in cnt.items():
            nums[v] += 1

        ret = 0
        for i in sorted(nums.keys(), reverse=True):
            while nums[i] > 1:
                j = i
                while j > 0 and nums[j] > 0:
                    j -= 1
                    ret += 1
                nums[j] += 1
                nums[i] -= 1
        return ret




def test():
    assert Solution().minDeletions(s = "aaaabbbcc") == 0
    assert Solution().minDeletions(s = "abcabc") == 3
    assert Solution().minDeletions(s = "aaabbbcc") == 2
    assert Solution().minDeletions(s = "ceabaacb") == 2


if __name__ == '__main__':
    test()

