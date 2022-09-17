#!/usr/bin/env python3
"""
CREATED AT: 2022-09-17

URL: https://leetcode.com/problems/palindrome-pairs/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 336-PalindromePairs

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Runtime: 3518 ms, faster than 78.86%
        Memory Usage: 26.5 MB, less than 52.30%

        1 <= words.length <= 5000
        0 <= words[i].length <= 300
        words[i] consists of lower-case English letters.
        """
        word_len_dict = collections.defaultdict(dict)
        for pos, word in enumerate(words):
            word_len_dict[len(word)][word] = pos

        len_list = sorted(word_len_dict.keys())

        ret = []

        def is_palindrome(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for pos, word in enumerate(words):
            for l in len_list:
                if l > len(word):
                    break
                if l == 0 and is_palindrome(word):
                    pos2 = word_len_dict[0]['']
                    if pos != pos2:
                        ret.extend([[pos, pos2], [pos2, pos]])
                    continue

                if is_palindrome(word[l:]):
                    missing_part = word[:l][::-1]
                    if missing_part in word_len_dict[l] and pos != word_len_dict[l][missing_part]:
                        ret.append([pos, word_len_dict[l][missing_part]])

                if l != len(word):
                    if is_palindrome(word[:-l]):
                        missing_part = word[-l:][::-1]
                        if missing_part in word_len_dict[l] and pos != word_len_dict[l][missing_part]:
                            ret.append([word_len_dict[l][missing_part], pos])
        return ret


def test():
    assert Solution().palindromePairs(words=["a", "b", "c", "ab", "ac", "aa"]) == [[3, 0], [1, 3], [4, 0], [2, 4],
                                                                                   [5, 0], [0, 5]]
    assert Solution().palindromePairs(words=["abcd", "dcba", "lls", "s", "sssll"]) == [[0, 1], [1, 0], [3, 2], [2, 4]]
    assert Solution().palindromePairs(words=["bat", "tab", "cat"]) == [[0, 1], [1, 0]]
    assert Solution().palindromePairs(words=["a", ""]) == [[0, 1], [1, 0]]


if __name__ == '__main__':
    test()
