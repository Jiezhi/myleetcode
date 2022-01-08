#!/usr/bin/env python
"""
CREATED AT: 2022/1/8
Des:

https://leetcode.com/contest/biweekly-contest-69/problems/longest-palindrome-by-concatenating-two-letter-words/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import collections
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        1 <= words.length <= 10^5
        words[i].length == 2
        words[i] consists of lowercase English letters.
        :param words:
        :return:
        """
        word_cnt = collections.Counter(words)
        ret = 0
        odd_flag = False
        for i in range(ord('a'), ord('z') + 1):
            for j in range(i, ord('z') + 1):
                word = f'{chr(i)}{chr(j)}'
                if i == j:
                    if word in word_cnt:
                        if (word_cnt[word] & 1) == 0:
                            ret += word_cnt[word] * 2
                        elif not odd_flag:
                            odd_flag = True
                            ret += word_cnt[word] * 2
                        else:
                            ret += (word_cnt[word] - 1) * 2
                else:
                    reword = f'{chr(j)}{chr(i)}'
                    if word in word_cnt and reword in word_cnt:
                        ret += min(word_cnt[word], word_cnt[reword]) * 4
        return ret


def test():
    assert Solution().longestPalindrome(words=["lc"]) == 0
    assert Solution().longestPalindrome(words=["ll"]) == 2
    assert Solution().longestPalindrome(words=["lc", "cl", "gg"]) == 6
    assert Solution().longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"]) == 8
    assert Solution().longestPalindrome(words=["cc", "ll", "xx"]) == 2


if __name__ == '__main__':
    test()
