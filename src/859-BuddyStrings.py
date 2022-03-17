#!/usr/bin/env python
"""
CREATED AT: 2022/3/17
Des:
https://leetcode.com/problems/buddy-strings/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        Runtime: 32 ms, faster than 93.20%
        Memory Usage: 14.1 MB, less than 97.50%

        1 <= s.length, goal.length <= 2 * 10^4
        s and goal consist of lowercase letters.
        """
        if len(s) != len(goal) or len(s) < 2:
            return False
        cnt = [0] * 26
        ord_a = ord('a')
        pos1, pos2 = None, None
        for i in range(len(s)):
            cnt[ord(s[i]) - ord_a] += 1
            if s[i] != goal[i]:
                if pos1 is None:
                    pos1 = i
                elif pos2 is None:
                    pos2 = i

                    if s[pos1] != goal[pos2] or s[pos2] != goal[pos1]:
                        return False
                else:
                    return False
        if pos1 is None and pos2 is None:
            return True if any(x > 1 for x in cnt) else False
        elif pos2 is None:
            return False
        return True


def test():
    assert Solution().buddyStrings("ab", "ba")
    assert Solution().buddyStrings("aa", "aa")


if __name__ == '__main__':
    test()
