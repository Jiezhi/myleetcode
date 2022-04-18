#!/usr/bin/env python
"""
CREATED AT: 2021/8/30
Des:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import Optional

import tree_node
from tree_node import TreeNode


class Solution:
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        """
        Runtime: 44 ms, faster than 98.45%
        Memory Usage: 18 MB, less than 48.12%

        The number of nodes in the tree is n.
        1 <= k <= n <= 10^4
        0 <= Node.val <= 10^4
        """

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        for i in inorder(root):
            if k > 1:
                k -= 1
            else:
                return i

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        93 / 93 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 18.1 MB
        :param root:
        :param k:
        :return:
        """
        cnt = 0
        stack = []
        tmp = root
        while tmp is not None or len(stack) > 0:
            if tmp is not None:
                stack.append(tmp)
                tmp = tmp.left
            elif len(stack) > 0:
                tmp = stack.pop()
                cnt += 1
                if cnt == k:
                    return tmp.val
                else:
                    tmp = tmp.right


def test():
    null = None
    assert Solution().kthSmallest(root=tree_node.build_tree_node([3, 1, 4, null, 2]), k=1) == 1
    assert Solution().kthSmallest(root=tree_node.build_tree_node([5, 3, 6, 2, 4, null, null, 1]), k=3) == 3
    
    assert Solution().kthSmallest2(root=tree_node.build_tree_node([3, 1, 4, null, 2]), k=1) == 1
    assert Solution().kthSmallest2(root=tree_node.build_tree_node([5, 3, 6, 2, 4, null, null, 1]), k=3) == 3


if __name__ == '__main__':
    test()
