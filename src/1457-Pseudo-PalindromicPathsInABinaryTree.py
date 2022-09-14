#!/usr/bin/env python3
"""
CREATED AT: 2022-09-14

URL: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1457-Pseudo-PalindromicPathsInABinaryTree

Difficulty: Medium

Desc: 

Tag: 

See: Bit manipulation https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/solution/

"""
from tool import *
from tree_node import TreeNode


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 2624 ms, faster than 5.30%
        Memory Usage: 50.4 MB, less than 94.70%
        The number of nodes in the tree is in the range [1, 10^5].
        1 <= Node.val <= 9
        """
        ret = 0
        count_odds = lambda l: sum(1 for x in l if (x & 1) == 1)
        stack = [(root, [0] * 10)]
        while stack:
            node, lst = stack.pop()
            lst[node.val] += 1
            if not node.left and not node.right:
                if count_odds(lst) <= 1:
                    ret += 1
            else:
                if node.left:
                    stack.append((node.left, lst.copy()))
                if node.right:
                    stack.append((node.right, lst.copy()))
        return ret


def test():
    assert Solution().pseudoPalindromicPaths(
        root=TreeNode.from_list([2, 1, 1, 1, 3, null, null, null, null, null, 1])) == 1
    assert Solution().pseudoPalindromicPaths(root=TreeNode.from_list([9])) == 1


if __name__ == '__main__':
    test()
