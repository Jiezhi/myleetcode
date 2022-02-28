#!/usr/bin/env python
"""
CREATED AT: 2021/9/22
Des:
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
https://leetcode.com/explore/item/3984
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
import collections
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        Solved 2022/2/28
        Runtime: 626 ms, faster than 16.57%
        Memory Usage: 14 MB, less than 81.13%

        1 <= arr.length <= 16
        1 <= arr[i].length <= 26
        arr[i] contains only lowercase English letters.
        """
        char_dict_list = collections.defaultdict(list)
        for s in arr:
            for c in s:
                char_dict_list[c].append(s)

        global_max_len = len(char_dict_list)

        def dfs(max_len, visited_char) -> int:
            if max_len == global_max_len:
                return max_len
            tmp_max_len = max_len
            for key, value in char_dict_list.items():
                if key in visited_char:
                    continue
                for v in value:
                    visited_char_copy = visited_char.copy()
                    valid_arr = True
                    for c in v:
                        if c in visited_char_copy:
                            valid_arr = False
                            break
                        else:
                            visited_char_copy.add(c)
                    if not valid_arr:
                        continue
                    tmp_max_len = max(tmp_max_len, dfs(max_len + len(v), visited_char_copy))
                    if tmp_max_len == global_max_len:
                        return tmp_max_len
            return tmp_max_len

        return dfs(0, set())


def test():
    assert Solution().maxLength(arr=["ab", "bc", "cd", "de", "ef", "fg", "gh", "hi"]) == 8
    assert Solution().maxLength(arr=["un", "iq", "ue"]) == 4
    assert Solution().maxLength(arr=["cha", "r", "act", "ers"]) == 6
    assert Solution().maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]) == 26
    assert Solution().maxLength(arr=[x for x in "abcdefghijklmnn"]) == 14
    assert Solution().maxLength(arr=[x for x in "abcdefghijklmnopqrstuvwxyz"]) == 26


if __name__ == '__main__':
    test()
