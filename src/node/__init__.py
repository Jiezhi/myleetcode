#!/usr/bin/env python
"""
Created on 2021/8/30

Des: Create for https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
from typing import List


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f'[val: {self.val}, left: {self.left}, right: {self.right}, next: {self.next}]'


def build_node_without_next(nums: List[int]) -> Node:
    if not nums:
        return None
    num_nodes = []
    for num in nums:
        if num is not None:
            num_nodes.append(Node(num))
        else:
            num_nodes.append(None)
    l = len(nums)
    i = 0
    nulls = 0
    while (i - nulls) <= (l / 2 - 1):
        if num_nodes[i]:
            num_nodes[i].left = num_nodes[2 * (i - nulls) + 1]
            if 2 * (i - nulls) + 2 < l:
                num_nodes[i].right = num_nodes[2 * (i - nulls) + 2]
        else:
            nulls += 1
        i += 1
    return num_nodes[0]


if __name__ == '__main__':
    pass
