#!/usr/bin/env python
"""
CREATED AT: 2022/4/24
Des:
https://leetcode.com/problems/binary-tree-maximum-path-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 2246

"""

from typing import Optional
from tree_node import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        The number of nodes in the tree is in the range [1, 3 * 10^4].
        -1000 <= Node.val <= 1000
        """
        ret = root.val

        def dfs(node) -> int:
            if not node:
                return -1000
            nonlocal ret
            if not node.left and not node.right:
                ret = max(ret, node.val)
                return node.val

            left = dfs(node.left)
            right = dfs(node.right)
            ret = max(ret, node.val, node.val + left, node.val + right, node.val + left + right, left, right)
            return max(node.val, node.val + left, node.val + right)

        dfs(root)
        return ret


def test():
    assert Solution().maxPathSum(TreeNode.from_list([-2, -1])) == -1
    assert Solution().maxPathSum(TreeNode.from_list([1, 2, 3])) == 6
    assert Solution().maxPathSum(TreeNode.from_list([-10, 9, 20, None, None, 15, 7])) == 42


if __name__ == '__main__':
    test()
