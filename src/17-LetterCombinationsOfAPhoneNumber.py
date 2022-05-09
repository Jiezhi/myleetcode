#!/usr/bin/env python
"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Created on 2018-12-28

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
import collections
from typing import List

num_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


class Solution:
    def letterCombinations2(self, digits: str) -> List[str]:
        """
        AC: 05/09/2022
        Runtime: 34 ms, faster than 76.96%
        Memory Usage: 13.9 MB, less than 79.68%
        :param digits: 0 <= digits.length <= 4
               digits[i] is a digit in the range ['2', '9']
        :return:
        """
        if not digits:
            return []
        digit_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        dq = collections.deque(list(digit_dict[digits[0]]))
        for i, d in enumerate(digits[1:], 1):
            while len(dq[0]) <= i:
                s = dq.popleft()
                for c in digit_dict[d]:
                    dq.append(s + c)
        return dq

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ret = ['']
        for d in digits:
            tmp_ret = []
            for r in ret:
                for l in num_dict[d]:
                    tmp_ret.append(r + l)
            ret = tmp_ret
        return ret


def test():
    assert set(Solution().letterCombinations('23')) == {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}
    assert set(Solution().letterCombinations2('23')) == {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}
    assert Solution().letterCombinations('') == []


if __name__ == '__main__':
    test()
