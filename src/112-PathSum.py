#!/usr/bin/env python
"""
CREATED AT: 2021/8/24
Des:
https://leetcode.com/problems/path-sum/
https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

import collections
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        116 / 116 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 15.8 MB
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return False
        dq = collections.deque()
        dq.append(root)
        while len(dq) > 0:
            node = dq.pop()
            if not node.left and not node.right and node.val == targetSum:
                return True
            if node.left:
                node.left.val += node.val
                dq.append(node.left)
            if node.right:
                node.right.val += node.val
                dq.append(node.right)
        return False


def test():
    null = None
    assert not Solution().hasPathSum(build_tree_node([]), 5)
    assert Solution().hasPathSum(build_tree_node([5]), 5)
    assert not Solution().hasPathSum(build_tree_node([4]), 5)
    assert Solution().hasPathSum(build_tree_node(
        [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]),
        targetSum=22)


if __name__ == '__main__':
    test()
