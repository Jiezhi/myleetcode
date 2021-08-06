#!/usr/bin/env python
"""
CREATED AT: 2021/8/6
Des:

https://leetcode.com/problems/n-ary-tree-level-order-traversal/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3871/

GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List

from ntree_node import Node


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        38 / 38 test cases passed.
        Status: Accepted
        Runtime: 44 ms
        Memory Usage: 16.1 MB
        :param root:
        :return:
        """
        if root is None or root.val is None:
            return []
        level_node = [[root]]
        current_level = 0
        while True:
            child_level_nodes = []
            for n in level_node[current_level]:
                if n is None or n.children is None:
                    continue
                for child in n.children:
                    child_level_nodes.append(child)
            if child_level_nodes:
                current_level += 1
                level_node.append(child_level_nodes)
            else:
                # if current_level is None or empty, then there's no node left to get
                break
        ret = [[x.val for x in level] for level in level_node]
        print(ret)
        return ret


def test():
    assert Solution().levelOrder(Node()) == []
    assert Solution().levelOrder(Node(val=1)) == [[1]]
    # TODO build nary tree from list
    # [0,null,10,2,null,1,9,1,null,2,0,4,2,null,6,8,0,null,9,10,null,3,1,7,null,9,8,1,2,6,null,6,7,10,null,7,null,null,4,null,4,10,8,7,10,null,null,6,0,null,3,null,8,7,3,null,8,null,0,7,3,null,null,null,0,4,4,2,null,9,5,1,4,0,null,1,4,9,10,3,null,null,7,7,0,8,1,null,3,2,10,null,2,4,0]
    # [[0],[10,2],[1,9,1,2,0,4,2],[6,8,0,9,10,3,1,7,9,8,1,2,6,6,7,10,7],[4,4,10,8,7,10,6,0,3,8,7,3,8,0,7,3,0,4,4,2,9,5,1,4,0,1,4,9,10,3,7,7,0,8,1,3,2,10,2,4,0]]


if __name__ == '__main__':
    test()
