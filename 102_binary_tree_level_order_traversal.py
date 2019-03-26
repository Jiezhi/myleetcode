#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-26

Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/

See also: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

"""
import queue
from tree_node import *


class Solution:
    def level_order(self, root: TreeNode) -> list:
        if not root:
            return []
        ret = []
        q = queue.Queue()
        q.put([root])
        while q.qsize() > 0:
            tmp_ret = []
            tmp_list = []
            for tmp in q.get():
                tmp_ret.append(tmp.val)
                if tmp.left:
                    tmp_list.append(tmp.left)
                if tmp.right:
                    tmp_list.append(tmp.right)
            ret.append(tmp_ret)
            if tmp_list:
                q.put(tmp_list)
        return ret


def test():
    assert Solution().level_order(build_tree_node([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]


if __name__ == '__main__':
    test()
