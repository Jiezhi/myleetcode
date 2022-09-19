#!/usr/bin/env python3
"""
CREATED AT: 2022-09-19

URL: https://leetcode.com/problems/find-duplicate-file-in-system/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 609-FindDuplicateFileInSystem

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        Runtime: 236 ms, faster than 13.56%
        Memory Usage: 24.1 MB, less than 54.58%

        1 <= paths.length <= 2 * 10^4
        1 <= paths[i].length <= 3000
        1 <= sum(paths[i].length) <= 5 * 10^5
        paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
        You may assume no files or directories share the same name in the same directory.
        You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.
        """
        cnt = collections.defaultdict(list)
        for path in paths:
            files = path.split(' ')
            folder = files[0]
            for file in files[1:]:
                segments = file.split('(')
                cnt[segments[1]].append(f'{folder}/{segments[0]}')
        ret = []
        for values in cnt.values():
            if len(values) > 1:
                ret.append(values)
        return ret


def test():
    ret = Solution().findDuplicate(
        paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
    assert len(ret) == len([["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]])
    ret = Solution().findDuplicate(
        paths=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)"])
    assert len(ret) == len([
        ["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]])


if __name__ == '__main__':
    test()
