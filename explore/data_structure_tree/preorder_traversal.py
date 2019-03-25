#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-18

Leetcode: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

same as problem 144.
"""
from tree_node import *


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root:
            return ret
        ret.append(root.val)
        if root.left:
            ret = ret + self.preorderTraversal(root.left)
        if root.right:
            ret = ret + self.preorderTraversal(root.right)
        return ret

    def preorderTraversal2(self, root: TreeNode) -> list:
        ret = []
        stack = []
        tmp = root
        while tmp:
            stack.append(tmp)
            ret.append(tmp.val)
            # add the root node and left child first
            while tmp.left:
                stack.append(tmp.left)
                ret.append(tmp.left.val)
                tmp = tmp.left
            tmp = stack.pop()
            # find the node who has a right child
            while stack and not tmp.right:
                tmp = stack.pop()
            if tmp.right:
                # find one and iterate the node
                tmp = tmp.right
            else:
                # there is no node has the right child
                return ret
        return ret

    # below are some other answers from leetcode(I reformat the code for cleaner code)
    def preorderTraversal3(self, root: TreeNode) -> list:
        if root is None:
            return []
        r = []
        s = [root]
        while s:
            n = s.pop()
            r.append(n.val)
            if n.right is not None:
                s.append(n.right)
            if n.left is not None:
                s.append(n.left)
        return r

    def preorderTraversal4(self, root: 'TreeNode') -> 'List[int]':
        ans = []
        p = root
        q = []
        while p is not None or len(q) > 0:
            while p is not None:
                ans.append(p.val)
                q.append(p)
                p = p.left
            if len(q) > 0:
                p = q.pop()
                p = p.right
        return ans


if __name__ == '__main__':
    assert Solution().preorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 2, 3]
    assert Solution().preorderTraversal2(build_tree_node([1, None, 2, 3])) == [1, 2, 3]
