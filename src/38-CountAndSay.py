#!/usr/bin/env python
"""
https://leetcode.com/problems/count-and-say/description/
Created on 2018-11-13

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def countAndSay2(self, n: int) -> str:
        """
        CREATED AT: 2022/2/15
        30 / 30 test cases passed.
        Status: Accepted
        Runtime: 40 ms, faster than 94.24%
        Memory Usage: 14 MB, less than 78.47%
        1 <= n <= 30
        """
        if n == 1:
            return '1'
        i = 1
        ret = '1'
        while i < n:
            i += 1
            pre_ret = ret
            pre_c = pre_ret[0]
            cnt = 1
            ret = ''
            for c in pre_ret[1:]:
                if c == pre_c:
                    cnt += 1
                else:
                    ret += f'{cnt}{pre_c}'
                    pre_c = c
                    cnt = 1
            ret = f'{ret}{cnt}{pre_c}'
        return ret

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n - 1):
            tmp = s[0]
            count = 0
            tmp_s = ""
            for c in s:
                if c == tmp:
                    count += 1
                else:
                    tmp_s += '{}{}'.format(count, tmp)
                    tmp = c
                    count = 1
            tmp_s += '{}{}'.format(count, tmp)
            s = tmp_s
        return s


def test():
    assert Solution().countAndSay(1) == "1"
    assert Solution().countAndSay(2) == "11"
    assert Solution().countAndSay(3) == "21"
    assert Solution().countAndSay(4) == "1211"
    assert Solution().countAndSay(5) == "111221"
    assert Solution().countAndSay2(5) == "111221"


if __name__ == '__main__':
    test()
