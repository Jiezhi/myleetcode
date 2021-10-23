#!/usr/bin/env python
"""
CREATED AT: 2021/8/19
Des:

https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3903/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

import collections
from typing import Optional

import tree_node
from tree_node import TreeNode


class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        54 / 54 test cases passed.
        Status: Accepted
        Runtime: 348 ms
        Memory Usage: 78.5 MB

        Hint1: If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

        :param root:
        :return:
        """

        # set node.val = all left sub nodes sum + node.val + all right sub nodes sum
        def sum_child(child: Optional[TreeNode]) -> int:
            if not child:
                return 0
            child.val += sum_child(child.left) + sum_child(child.right)
            return child.val

        sum_child(root)

        # cut the line and calculate the product of two subtrees
        dq = collections.deque()
        dq.append(root)
        max_ret = 0
        while len(dq) > 0:
            node = dq.pop()
            if node.left:
                max_ret = max(max_ret, node.left.val * (root.val - node.left.val))
                dq.append(node.left)
            if node.right:
                max_ret = max(max_ret, node.right.val * (root.val - node.right.val))
                dq.append(node.right)
        return max_ret % (10 ** 9 + 7)


def test():
    null = None
    assert Solution().maxProduct(tree_node.build_tree_node([1, 2, 3, 4, 5, 6])) == 110
    assert Solution().maxProduct(tree_node.build_tree_node([1, null, 2, 3, 4, null, null, 5, 6])) == 90
    assert Solution().maxProduct(tree_node.build_tree_node([2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1])) == 1025
    assert Solution().maxProduct(tree_node.build_tree_node([1, 1])) == 1


if __name__ == '__main__':
    test()
