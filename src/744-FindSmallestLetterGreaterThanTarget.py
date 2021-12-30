#!/usr/bin/env python
"""
CREATED AT: 2021/12/30
Des:

https://leetcode.com/problems/find-smallest-letter-greater-than-target/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        165 / 165 test cases passed.
        Status: Accepted
        Runtime: 136 ms
        Memory Usage: 14.9 MB
        2 <= letters.length <= 10^4
        letters[i] is a lowercase English letter.
        letters is sorted in non-decreasing order.
        letters contains at least two different characters.
        target is a lowercase English letter.
        :param letters:
        :param target:
        :return:
        """
        if target >= letters[-1]:
            return letters[0]
        low, high = 0, len(letters) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            if letters[mid] <= target:
                low = mid
            else:
                high = mid
        # low + 1 == high
        if letters[low] > target:
            return letters[low]
        return letters[high] if letters[high] != target else letters[high + 1]


def test():
    assert Solution().nextGreatestLetter(letters=["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], target="e") == "n"
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a") == "c"
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="c") == 'f'
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="d") == 'f'
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="f") == 'j'
    assert Solution().nextGreatestLetter(letters=["c", "f", "j"], target="j") == 'c'


if __name__ == '__main__':
    test()
