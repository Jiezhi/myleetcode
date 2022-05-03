#!/usr/bin/env python
"""
CREATED AT: 2022/5/3
Des:
https://leetcode.com/problems/reorder-data-in-log-files/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import string
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        Runtime: 67 ms, faster than 18.89%
        Memory Usage: 13.9 MB, less than 97.84%

        1 <= logs.length <= 100
        3 <= logs[i].length <= 100
        All the tokens of logs[i] are separated by a single space.
        logs[i] is guaranteed to have an identifier and at least one word after the identifier.
        """
        letter_ret = []
        digit_ret = []
        for log in logs:
            space_pos = log.index(' ')
            if log[space_pos + 1] in string.digits:
                digit_ret.append(log)
            else:
                insert_pos = len(letter_ret)
                for i, tmp in enumerate(letter_ret):
                    tmp_pos = tmp.index(' ')
                    if log[space_pos + 1:] < tmp[tmp_pos + 1:]:
                        insert_pos = i
                        break
                    elif log[space_pos + 1:] == tmp[tmp_pos + 1:]:
                        if log[:space_pos] < tmp[:tmp_pos]:
                            insert_pos = i
                            break
                letter_ret.insert(insert_pos, log)
        return letter_ret + digit_ret


def test():
    assert Solution().reorderLogFiles(
        logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    ) == ["let1 art can",
          "let3 art zero",
          "let2 own kit dig",
          "dig1 8 1 5 1",
          "dig2 3 6"]


if __name__ == '__main__':
    test()
