"""
CREATED AT: 2022/10/7
Des:

GITHUB: https://github.com/Jiezhi/myleetcode
https://leetcode.cn/contest/season/2022-fall/problems/KnLfVT/
https://leetcode.cn/problems/KnLfVT/
Difficulty: Easy

Tag:

See:

Time Spent:  min
"""
from collections import Counter
from typing import List, Optional

from src.tree_node import TreeNode


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                tn = TreeNode(-1, left=node.left)
                node.left = tn
                stack.append(tn.left)
            if node.right:
                tn = TreeNode(-1, right=node.right)
                node.right = tn
                stack.append(tn.right)
        return root


def test():
    null = None
    assert Solution().expandBinaryTree(root=TreeNode.from_list([7, 5, 6])) == TreeNode.from_list(
        [7, -1, -1, 5, null, null, 6])


if __name__ == '__main__':
    test()
