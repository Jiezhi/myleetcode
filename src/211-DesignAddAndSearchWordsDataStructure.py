#!/usr/bin/env python
"""
CREATED AT: 2022/1/28
Des:

https://leetcode.com/problems/design-add-and-search-words-data-structure/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""


class WordDictionary:
    """
    CREATED AT: 2022/1/28
    1 <= word.length <= 500
    word in addWord consists lower-case English letters.
    word in search consist of  '.' or lower-case English letters.
    At most 50000 calls will be made to addWord and search.
    """

    def __init__(self):
        self.root = dict()
        pass

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]
        cur['#'] = []

    def search(self, word: str) -> bool:
        def dfs(word, cur) -> bool:
            if len(word) == 0 and '#' in cur:
                return True
            for c in word:
                if c == '.':
                    return any(dfs(word[1:], cur[next_dict]) for next_dict in cur)
                if c not in cur:
                    return False
                else:
                    return dfs(word[1:], cur[c])

        return dfs(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def test():
    wd = WordDictionary()
    wd.addWord("test")
    assert wd.search("test")
    assert wd.search("te.t")
    assert wd.search("tes.")
    assert not wd.search("tes..")
    assert not wd.search("tr.t")


if __name__ == '__main__':
    test()
