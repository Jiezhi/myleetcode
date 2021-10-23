#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.

https://leetcode.com/problems/fizz-buzz/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/743/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        8 / 8 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 15.1 MB
        :param n:
        :return:
        """
        ret = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ret.append('FizzBuzz')
            elif i % 3 == 0:
                ret.append('Fizz')
            elif i % 5 == 0:
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret


def test():
    assert Solution().fizzBuzz(n=3) == ["1", "2", "Fizz"]
    assert Solution().fizzBuzz(n=5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert Solution().fizzBuzz(n=15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz",
                                         "13", "14", "FizzBuzz"]


if __name__ == '__main__':
    test()
