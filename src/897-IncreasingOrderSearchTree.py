#!/usr/bin/env python
"""
CREATED AT: 2022/4/17
Des:
https://leetcode.com/problems/increasing-order-search-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: https://leetcode.com/problems/increasing-order-search-tree/solution/
 https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
 for more solutions

"""

from tree_node import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        Runtime: 39 ms, faster than 66.24%
        Memory Usage: 14 MB, less than 50.58%

        :param root:
        The number of nodes in the given tree will be in the range [1, 100].
        0 <= Node.val <= 1000
        :return:
        """

        def dfs(node):
            if not node:
                return None, None
            if not node.left and not node.right:
                return node, node
            lhead, ltail = dfs(node.left)
            rhead, rtail = dfs(node.right)
            if ltail:
                ltail.right = node
            else:
                lhead = node
            if rhead:
                node.right = rhead
            else:
                rtail = node
            node.left = None
            return lhead, rtail

        ret, _ = dfs(root)
        return ret


def test():
    pass


if __name__ == '__main__':
    test()
