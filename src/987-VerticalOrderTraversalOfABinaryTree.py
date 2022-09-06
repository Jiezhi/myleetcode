#!/usr/bin/env python3
"""
CREATED AT: 2022-09-05

URL: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 987-VerticalOrderTraversalOfABinaryTree

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Runtime: 66 ms, faster than 25.00%
        Memory Usage: 14.2 MB, less than 28.66%

        The number of nodes in the tree is in the range [1, 1000].
        0 <= Node.val <= 1000
        """
        col_map = collections.defaultdict(list)
        stack = [(root, 0, 0)]
        max_col = 0
        while stack:
            node, col, row = stack.pop()
            col_map[col].append((node.val, row))
            max_col = max(max_col, abs(col))
            if node.left:
                stack.append((node.left, col - 1, row + 1))
            if node.right:
                stack.append((node.right, col + 1, row + 1))
        ret = []
        for i in range(-max_col, max_col + 1):
            if col_map[i]:
                tmp = col_map[i]
                ret.append(list(v[0] for v in sorted(tmp, key=lambda x: (x[1], x[0]))))
        return ret


def test():
    assert Solution().verticalTraversal(root=TreeNode.from_list([3, 9, 20, null, null, 15, 7])) == [[9], [3, 15], [20],
                                                                                                    [7]]
    assert Solution().verticalTraversal(root=TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])) == [[4], [2], [1, 5, 6], [3],
                                                                                            [7]]
    assert Solution().verticalTraversal(root=TreeNode.from_list([1, 2, 3, 4, 6, 5, 7])) == [[4], [2], [1, 5, 6], [3],
                                                                                            [7]]


if __name__ == '__main__':
    test()
