#!/usr/bin/env python
"""
CREATED AT: 2021/9/2
Des:
https://leetcode.com/problems/binary-search-tree-iterator/
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/1008/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections
from typing import Optional

from tree_node import TreeNode, build_tree_node


class BSTIterator2:
    """
    AC: 04/20/2022 15:25
    Runtime: 88 ms, faster than 63.31%
    Memory Usage: 20.4 MB, less than 63.85%

    The number of nodes in the tree is in the range [1, 10^5].
    0 <= Node.val <= 10^6
    At most 10^5 calls will be made to hasNext, and next.
    """

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root

    def next(self) -> int:
        while self.cur:
            if self.cur.left:
                tmp = self.cur.left
                while tmp.right and tmp.right != self.cur:
                    tmp = tmp.right
                if tmp.right == self.cur:
                    tmp.right = None
                    ret = self.cur.val
                    self.cur = self.cur.right
                    return ret
                else:
                    tmp.right = self.cur
                    self.cur = self.cur.left
            else:
                ret = self.cur.val
                self.cur = self.cur.right
                return ret

    def hasNext(self) -> bool:
        return self.cur is not None


class BSTIterator:
    """
    61 / 61 test cases passed.
    Status: Accepted
    Runtime: 105 ms
    Memory Usage: 20.7 MB
    """

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.dq = collections.deque()
        tmp_node = self.root
        while tmp_node is not None:
            self.dq.append(tmp_node)
            tmp_node = tmp_node.left

    def next(self) -> int:
        tmp_node = self.dq.pop()
        val = tmp_node.val
        tmp_node = tmp_node.right
        while tmp_node is not None:
            self.dq.append(tmp_node)
            tmp_node = tmp_node.left
        return val

    def hasNext(self) -> bool:
        return len(self.dq) > 0


def test():
    null = None
    bst_iterator = BSTIterator(build_tree_node([7, 3, 15, null, null, 9, 20]))
    assert bst_iterator.next() == 3
    assert bst_iterator.next() == 7
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == 9
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == 15
    assert bst_iterator.hasNext()
    assert bst_iterator.next() == 20
    assert not bst_iterator.hasNext()


if __name__ == '__main__':
    test()
