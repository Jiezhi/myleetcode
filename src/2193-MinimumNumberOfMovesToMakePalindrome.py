#!/usr/bin/env python
"""
CREATED AT: 2022/3/7
Des:
https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        Ref: https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/discuss/1822174/C%2B%2BPython-Short-Greedy-Solution
        Runtime: 84 ms, faster than 100.00%
        Memory Usage: 14.1 MB, less than 42.86%

        1 <= s.length <= 2000
        s consists only of lowercase English letters.
        s can be converted to a palindrome using a finite number of moves.
        """
        str_list = list(s)
        ret = 0
        while str_list:
            pos = str_list.index(str_list[-1])
            # only one letter and should be middle of the str
            if pos == len(str_list) - 1:
                ret += len(str_list) // 2
                str_list.pop()
            else:
                ret += pos
                str_list.pop()
                str_list.pop(pos)
        return ret


def test():
    assert Solution().minMovesToMakePalindrome("aabbcc") == 6
    assert Solution().minMovesToMakePalindrome("aabb") == 2
    assert Solution().minMovesToMakePalindrome("letelt") == 2
    assert Solution().minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii") == 163


if __name__ == '__main__':
    test()
