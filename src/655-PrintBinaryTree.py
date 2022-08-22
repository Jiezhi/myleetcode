#!/usr/bin/env python3
"""
CREATED AT: 2022-08-22

URL: https://leetcode.com/problems/print-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 655-PrintBinaryTree

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        Runtime: 62 ms, faster than 26.46%
        Memory Usage: 13.9 MB, less than 46.06%

        The number of nodes in the tree is in the range [1, 2^10].
        -99 <= Node.val <= 99
        The depth of the tree will be in the range [1, 10].
        """

        def get_height(tree) -> int:
            if not tree:
                return 0
            ret = 0
            stack = [(tree, 1)]
            while stack:
                node, height = stack.pop()
                ret = max(ret, height)
                if node.left:
                    stack.append((node.left, height + 1))
                if node.right:
                    stack.append((node.right, height + 1))
            return ret

        m = get_height(root)
        n = 2 ** m - 1
        matrix = [["" for _ in range(n)] for _ in range(m)]

        def fill(i, j, node):
            if not node:
                return
            print(i, j, node.val)
            matrix[i][j] = str(node.val)
            fill(i + 1, j - 2 ** (m - i - 2), node.left)
            fill(i + 1, j + 2 ** (m - i - 2), node.right)

        fill(0, (n - 1) // 2, root)

        return matrix


def test():
    assert Solution().printTree(root=TreeNode.from_list([1, 2])) == [["", "1", ""], ["2", "", ""]]
    assert Solution().printTree(root=TreeNode.from_list([1, 2, 3, null, 4])) == [["", "", "", "1", "", "", ""],
                                                                                 ["", "2", "", "", "", "3", ""],
                                                                                 ["", "", "4", "", "", "", ""]]


if __name__ == '__main__':
    test()
