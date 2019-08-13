#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-05-07

Leetcode: https://leetcode.com/problems/path-sum/

https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/

"""
from tree_node import *


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = []
        val_stack = []
        ret = 0
        tmp = root
        while tmp or len(stack) > 0:
            if tmp:
                ret += tmp.val
                val_stack.append(tmp.val)
                if not tmp.left and not tmp.right:
                    if ret == sum:
                        return True
                    else:
                        ret -= val_stack.pop()
                        tmp = stack.pop()
                stack.append(tmp.right)
                tmp = tmp.left
            else:
                # ret -= val_stack.pop()
                tmp = stack.pop()
        return False


def test():
    assert Solution().hasPathSum(build_tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22)
    assert not Solution().hasPathSum(build_tree_node([-2, None, -3]), -3)
    assert not Solution().hasPathSum(build_tree_node([1, -2, -3, 1, 3, -2, None, -1]), 3)


if __name__ == '__main__':
    test()
