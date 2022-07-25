#!/usr/bin/env python3
"""
CREATED AT: 2022-07-25

URL: https://leetcode.com/problems/complete-binary-tree-inserter/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 919-CompleteBinaryTreeInserter

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *
from tree_node import TreeNode


class CBTInserter:
    """
    Runtime: 119 ms, faster than 47.35% 
    Memory Usage: 15.1 MB, less than 26.79% 
    The number of nodes in the tree will be in the range [1, 1000].
    0 <= Node.val <= 5000
    root is a complete binary tree.
    0 <= val <= 5000
    At most 10^4 calls will be made to insert and get_root.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.dq = collections.deque([root])

    def insert(self, val: int) -> int:
        while self.dq:
            node = self.dq[0]
            if not node.left:
                node.left = TreeNode(val)
                return node.val
            elif not node.right:
                node.right = TreeNode(val)
                self.dq.append(node.left)
                self.dq.append(node.right)
                self.dq.popleft()
                return node.val
            else:
                self.dq.append(node.left)
                self.dq.append(node.right)
                self.dq.popleft()

    def get_root(self) -> Optional[TreeNode]:
        return self.root


def test():
    obj = CBTInserter(TreeNode.from_list([1, 2]))
    assert obj.insert(3) == 1
    assert obj.insert(4) == 2
    assert obj.get_root() == TreeNode.from_list([1, 2, 3, 4])

    obj = CBTInserter(TreeNode.from_list([1, 2, 3]))
    assert obj.insert(4) == 2
    assert obj.insert(5) == 2
    assert obj.insert(6) == 3
    assert obj.insert(7) == 3
    assert obj.insert(8) == 4
    assert obj.get_root() == TreeNode.from_list([1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    test()
