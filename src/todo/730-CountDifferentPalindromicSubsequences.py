#!/usr/bin/env python3
"""
CREATED AT: 2022-06-10

URL: https://leetcode.com/problems/count-different-palindromic-subsequences/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 730-CountDifferentPalindromicSubsequences

Difficulty: Hard

Desc: Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 10^9 + 7.

A subsequence of a string is obtained by deleting zero or more characters from the string.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences a1, a2, ... and b1, b2, ... are different if there is some i for which ai != bi.


Tag: 

See: 

"""
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        """
        1 <= s.length <= 1000
        s[i] is either 'a', 'b', 'c', or 'd'.
        """
        MOD = 10 ** 9 + 7
        
        def dp(i, j) -> (int, set):
            distinct = set()
            if i > j:
                return (0, distinct)
            if i == j:
                distinct.add(s[i])
                return (1, distinct)
            ret = 0
            for c in 'abcd':
                l = s.find(c, i, j)
                if l < 0:
                    continue
                r = s.rfind(c, i, j)
                sub_ret, sub_set = dp(l, r)
                print(sub_ret, sub_set)
                # print(f'{c}-{sub_set}-{c}')
                ret += sub_ret + 1
                ret %= MOD
                distinct.union(sub_set)
                distinct.add(c)

            return ret, distinct
        return dp(0, len(s))[0]


def test():
    assert Solution().countPalindromicSubsequences(s="bccb") == 6
    assert Solution().countPalindromicSubsequences(s="abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361


if __name__ == '__main__':
    test()

