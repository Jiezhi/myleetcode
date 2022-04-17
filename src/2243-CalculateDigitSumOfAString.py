#!/usr/bin/env python
"""
CREATED AT: 2022/4/17
Des:
https://leetcode.com/problems/calculate-digit-sum-of-a-string/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """
        1 <= s.length <= 100
        2 <= k <= 100
        s consists of digits only.
        """
        if len(s) <= k:
            return s
        new_str = ''
        for i in range(0, len(s) // k + 1):
            if i * k >= len(s):
                break
            exp = '+'.join([x for x in s[i * k: (i + 1) * k]])
            new_str += str(eval(exp))
        return self.digitSum(new_str, k)


def test():
    assert Solution().digitSum(s="11111222223", k=3) == "135"
    assert Solution().digitSum(s="00000000", k=3) == "000"


if __name__ == '__main__':
    test()
