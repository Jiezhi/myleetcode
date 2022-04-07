#!/usr/bin/env python
"""
CREATED AT: 2022/4/7
Des:
https://leetcode.com/problems/lemonade-change/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Runtime: 1066 ms, faster than 53.66%
        Memory Usage: 17.5 MB, less than 98.43%
        
        :param bills: 1 <= bills.length <= 10^5
                      bills[i] is either 5, 10, or 20.
        :return:
        """
        m5, m10 = 0, 0
        for bill in bills:
            if bill == 10:
                if m5 <= 0:
                    return False
                m5 -= 1
                m10 += 1
            elif bill == 20:
                if m5 <= 0:
                    return False
                if m10 <= 0:
                    if m5 < 3:
                        return False
                    m5 -= 3
                else:
                    m5 -= 1
                    m10 -= 1
            else:
                m5 += 1
        return True


def test():
    assert Solution().lemonadeChange([5, 5, 5, 10, 20])
    assert not Solution().lemonadeChange([5, 5, 10, 10, 20])


if __name__ == '__main__':
    test()
