#!/usr/bin/env python
"""
CREATED AT: 2022/3/14
Des:
https://leetcode.com/problems/simplify-path/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Runtime: 91 ms, faster than 5.02%
        Memory Usage: 14 MB, less than 32.22%
        
        1 <= path.length <= 3000
        path consists of English letters, digits, period '.', slash '/' or '_'.
        path is a valid absolute Unix path.
        """
        ret = []
        i = 0
        word_start = None
        while i < len(path):
            if path[i] == '/':
                if word_start:
                    ret.append(path[word_start: i])
                    word_start = None
                if not (ret and ret[-1] == '/'):
                    ret.append('/')
                i += 1
                continue
            elif path[i] == '.':
                # if word_start:
                #     ret.append(path[word_start, i])
                #     word_start = None
                if i < len(path) - 1:
                    if path[i + 1] == '/':
                        i += 2
                        continue

                    if path[i + 1] == '.':
                        if i < len(path) - 2:
                            if path[i + 2] == '/':
                                if ret:
                                    ret.pop()
                                if ret:
                                    ret.pop()
                                i += 3
                                continue
                            tmp_i = i + 2
                            while tmp_i < len(path) and path[tmp_i] == '.':
                                tmp_i += 1
                            if not word_start:
                                word_start = i
                            if tmp_i < len(path):
                                # more than two dots

                                if path[tmp_i] == '/':
                                    ret.append(path[word_start: tmp_i])
                                    word_start = None
                            i = tmp_i
                            continue
                        else:
                            # last two char ..
                            if word_start:
                                ret.append(path[word_start:])
                                word_start = None
                            else:
                                if ret:
                                    ret.pop()
                                if ret:
                                    ret.pop()
                    else:
                        # path[i + 1] not in ['.', '/']
                        if not word_start:
                            word_start = i
            else:
                if not word_start:
                    word_start = i
            i += 1
        if word_start:
            ret.append(path[word_start:])
        if len(ret) > 1 and ret[-1] == '/':
            ret.pop()
        if not ret:
            return '/'
        ret = ''.join(ret)
        if ret[0] != '/':
            return '/' + ret
        else:
            return ret


def test():
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath("/a/../../b/../c//.//") == "/c"
    assert Solution().simplifyPath("/a//b////c/d//././/..") == "/a/b/c"
    assert Solution().simplifyPath("/a//b////c/d//././/...") == "/a/b/c/d/..."
    assert Solution().simplifyPath("/..hidden") == "/..hidden"
    assert Solution().simplifyPath("/..../abc/.././xyz/./ef/../.") == "/..../xyz"


if __name__ == '__main__':
    test()
