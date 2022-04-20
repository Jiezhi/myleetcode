"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
 @Author: Jiezhi 
 @Date: 2018-07-06 17:44:55 
 @Last Modified by:   Jiezhi 
 @Last Modified time: 2018-07-06 17:44:55 
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr = ''
        max_len = 0
        for c in s:
            if c not in max_substr:
                max_substr += c
            else:
                max_len = max(len(max_substr), max_len)
                max_substr = max_substr[max_substr.index(c) + 1:]
                max_substr += c
        max_len = max(len(max_substr), max_len)
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        20210828 do it again,
        and found the solution thought is same like 3 years ago(2018-07-06)
        987 / 987 test cases passed.
        Status: Accepted
        Runtime: 57 ms
        Memory Usage: 14.2 MB
        :param s:
        :return:
        """
        subs = ''
        longest_len = 0
        for i in s:
            if i in subs:
                longest_len = max(len(subs), longest_len)
                subs = subs[subs.index(i) + 1:]
            subs += i
        longest_len = max(len(subs), longest_len)
        return longest_len

    def lengthOfLongestSubstring3(self, s: str) -> int:
        """
        Update at 2022/04/20
        Runtime: 90 ms, faster than 55.33%
        Memory Usage: 14 MB, less than 94.07%
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.
        """
        if len(s) < 2:
            return len(s)
        ret = 0
        char_set = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            else:
                char_set.add(s[r])
                r += 1
                ret = max(ret, len(char_set))
        return ret


def test():
    assert Solution().lengthOfLongestSubstring('abcdcfge') == 5

    assert Solution().lengthOfLongestSubstring2('') == 0
    assert Solution().lengthOfLongestSubstring2(s="abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring2(s="bbbbb") == 1
    assert Solution().lengthOfLongestSubstring2(s="pwwkew") == 3
    assert Solution().lengthOfLongestSubstring2('abcdcfge') == 5

    assert Solution().lengthOfLongestSubstring3(s="abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring3(s="bbbbb") == 1
    assert Solution().lengthOfLongestSubstring3(s="pwwkew") == 3
    assert Solution().lengthOfLongestSubstring3('abcdcfge') == 5


if __name__ == '__main__':
    test()
