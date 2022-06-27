#!/usr/bin/env python
"""
CREATED AT: 2022/2/28
Des:

https://leetcode.com/problems/maximum-width-of-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""

from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 79 ms, faster than 25.28%
        Memory Usage: 14.9 MB, less than 69.37%
        The number of nodes in the tree is in the range [1, 3000].
        -100 <= Node.val <= 100
        """
        ret = 0
        curr_level = [(root, 0)]
        while curr_level:
            ret = max(ret, curr_level[-1][1] - curr_level[0][1] + 1)
            next_level = []
            for node, pos in curr_level:
                if node.left:
                    next_level.append((node.left, pos * 2))

                if node.right:
                    next_level.append((node.right, pos * 2 + 1))

            curr_level = next_level
        return ret


def test():
    null = None
    assert Solution().widthOfBinaryTree(build_tree_node([1, 3, 2, 5, 3, null, 9])) == 4


if __name__ == '__main__':
    test()
