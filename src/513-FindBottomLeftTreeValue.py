#!/usr/bin/env python3
"""
CREATED AT: 2022-06-22

URL: https://leetcode.com/problems/find-bottom-left-tree-value/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 513-FindBottomLeftTreeValue

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import Optional

from tree_node import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 81 ms, faster than 22.04%
        Memory Usage: 16.4 MB, less than 32.58%
        The number of nodes in the tree is in the range [1, 10^4].
        -2^31 <= Node.val <= 2^31 - 1
        """
        ret = root.val
        cur_level = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level > cur_level:
                cur_level = level
                ret = node.val
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return ret


def test():
    null = None
    assert Solution().findBottomLeftValue(root=TreeNode.from_list([2, 1, 3])) == 1
    assert Solution().findBottomLeftValue(root=TreeNode.from_list([1, 2, 3, 4, null, 5, 6, null, null, 7])) == 7


if __name__ == '__main__':
    test()
