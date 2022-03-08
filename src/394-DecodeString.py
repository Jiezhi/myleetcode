#!/usr/bin/env python
"""
CREATED AT: 2022/3/8
Des:

https://leetcode.com/problems/decode-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Runtime: 32 ms, faster than 84.49%
        Memory Usage: 13.9 MB, less than 48.99%

        1 <= s.length <= 30
        s consists of lowercase English letters, digits, and square brackets '[]'.
        s is guaranteed to be a valid input.
        All the integers in s are in the range [1, 300].
        """
        if '[' not in s:
            return s
        left_pos = s.index('[')
        right_pos = left_pos + 2
        left_square_cnt = 1
        while left_square_cnt > 0:
            if s[right_pos] == '[':
                left_square_cnt += 1
            elif s[right_pos] == ']':
                left_square_cnt -= 1
            right_pos += 1
        right_pos -= 1
        num_start = left_pos - 1
        while num_start >= 0 and str.isdigit(s[num_start]):
            num_start -= 1
        num_start += 1
        if right_pos < len(s) - 1:
            right_str = s[right_pos + 1:]
        else:
            right_str = ''
        return s[:num_start] + int(s[num_start:left_pos]) * self.decodeString(
            s[left_pos + 1: right_pos]) + self.decodeString(right_str)


def test():
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"


if __name__ == '__main__':
    test()
