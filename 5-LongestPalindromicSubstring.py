#!/usr/bin/env python
"""
https://leetcode.com/problems/longest-palindromic-substring/description/
Created on 11/19/18

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    # 这个方法遇到长字符串在leetcode会超时
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        for i in range(l):
            for j in range(i + 1):
                # print(s[j:l - i + j])
                if isPalindrome(s[j:l - i + j]):
                    return s[j:l - i + j]
        # May be a empty str
        return s

    # 可参考https://segmentfault.com/a/1190000003914228
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        RL = [0] * len(s)
        maxRight = 0
        pos = 0
        maxLen = 0
        for i in range(len(s)):
            if i < maxRight:
                RL[i] = min(RL[2 * pos - i], maxRight - i)
            else:
                RL[i] = 1

            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1

            if RL[i] + i - 1 > maxRight:
                maxRight = RL[i] + i - 1
                pos = i

            maxLen = max(maxLen, RL[i])

        # 如果只返回长度的话：
        # return maxLen - 1

        maxPos = RL.index(maxLen)
        return s[maxPos - maxLen + 1: maxPos + maxLen].replace('#', '')

    def longestPalindrome3(self, s):
        """
        TODO 动态规划
        :type s: str
        :rtype: str
        """
        pass


def isPalindrome(s):
    """
    :param s:
    :return:
    """
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


def test():
    assert isPalindrome('bab')
    assert isPalindrome('bb')
    assert not isPalindrome('abc')
    assert Solution().longestPalindrome("") == ""
    assert Solution().longestPalindrome('babad') == 'bab'
    assert Solution().longestPalindrome('cbbd') == 'bb'
    assert Solution().longestPalindrome2("bab") == 'bab'
    assert Solution().longestPalindrome2("1baab2") == 'baab'
    assert Solution().longestPalindrome2("45666666baabaab123") == 'baabaab'
