#!/usr/bin/env python3
"""
CREATED AT: 2022-08-05

URL: https://leetcode.com/problems/add-one-row-to-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 623-AddOneRowToTree

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        Runtime: 94 ms, faster than 39.67%
        Memory Usage: 16.7 MB, less than 66.86%

        The number of nodes in the tree is in the range [1, 10^4].
        The depth of the tree is in the range [1, 10^4].
        -100 <= Node.val <= 100
        -10^5 <= val <= 10^5
        1 <= depth <= the depth of tree + 1
        """
        if depth == 1:
            return TreeNode(val, left=root)
        dq = collections.deque([(root, 1)])
        while dq:
            node, dep = dq.popleft()
            if dep == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, right=node.right)
            else:
                if node.left:
                    dq.append((node.left, dep + 1))
                if node.right:
                    dq.append((node.right, dep + 1))
        return root


def test():
    assert Solution().addOneRow(root=TreeNode.from_list([4, 2, 6, 3, 1, 5]), val=1, depth=2) == TreeNode.from_list(
        [4, 1, 1, 2, null, null, 6, 3, 1, 5])
    assert Solution().addOneRow(root=TreeNode.from_list([4, 2, null, 3, 1]), val=1, depth=3) == TreeNode.from_list(
        [4, 2, null, 1, 1, 3, null, null, 1])
    assert Solution().addOneRow(root=TreeNode.from_list([1, 2, 3, 4]), val=5, depth=4) == TreeNode.from_list(
        [1, 2, 3, 4, null, null, null, 5, 5])


if __name__ == '__main__':
    test()
