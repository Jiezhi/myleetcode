#!/usr/bin/env python
"""
CREATED AT: 2021/9/1
Des:
https://leetcode.com/problems/generate-parentheses/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        8 / 8 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.7 MB
        :param n:
        :return:
        """
        if n == 1:
            return ["()"]
        ret = self.generateParenthesis(n - 1)
        ret_set = set()
        for p in ret:
            ret_set.add(f'(){p}')
            ret_set.add(f'{p}()')
            for i in range(len(p)):
                if p[i] == '(':
                    ret_set.add(f'{p[:i + 1]}(){p[i + 1:]}')
        return list(ret_set)


def test():
    assert Solution().generateParenthesis(n=1) == ["()"]

    ans = ["()()", "(())"]
    ret = Solution().generateParenthesis(n=2)
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret

    ans = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    ret = Solution().generateParenthesis(n=3)
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret

    ans = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()",
           "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
    ret = Solution().generateParenthesis(n=4)
    assert len(ret) == len(ans)
    for a in ans:
        assert a in ret

    ret = Solution().generateParenthesis(n=8)
    print(ret)


if __name__ == '__main__':
    test()
