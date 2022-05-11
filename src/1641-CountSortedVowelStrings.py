#!/usr/bin/env python
"""
CREATED AT: 2022/5/11
Des:
https://leetcode.com/problems/count-sorted-vowel-strings/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections


class Solution:
    def countVowelStrings(self, n: int) -> int:
        """
        Runtime: 61 ms, faster than 26.05%
        Memory Usage: 13.9 MB, less than 65.31%
        1 <= n <= 50
        :param n:
        :return:
        """
        pre = [1] * 5
        cur = pre
        for i in range(1, n):
            for j in range(1, 5):
                cur[j] = cur[j - 1] + pre[j]
            pre = cur
        return sum(cur)

    def countVowelStrings2(self, n: int) -> int:
        """
        1 <= n <= 50
        LTE
        """
        ret = 0
        vowels = 'aeiou'
        dq = collections.deque(list(vowels))
        while dq:
            node = dq.popleft()
            if len(node) == n:
                ret += 1
                continue
            pos = vowels.index(node[-1])
            for c in vowels[pos:]:
                dq.append(node + c)

        return ret


def test():
    assert Solution().countVowelStrings2(1) == 5
    assert Solution().countVowelStrings2(50) == 316251

    assert Solution().countVowelStrings(1) == 5
    assert Solution().countVowelStrings(50) == 316251


if __name__ == '__main__':
    test()
