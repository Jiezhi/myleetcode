#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/10/17
Updated on 2021/10/25

Leetcode:  https://leetcode.com/problems/min-stack/

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/

Difficulty: Easy

Tags: Design
"""
import collections


class MinStack:
    """
    Updated on 2021/10/25
    Runtime: 85 ms, faster than 46.80%
    Memory Usage: 18 MB, less than 80.67%
    -2**31 <= val <= 23**1 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 10**4 calls will be made to push, pop, top, and getMin.
    """

    def __init__(self):
        self.data_stack = collections.deque()
        self.min_stack = collections.deque()

    def push(self, val: int) -> None:
        self.data_stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if len(self.data_stack) > 0:
            self.data_stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.data_stack) > 0:
            return self.data_stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:

def test():
    obj = MinStack()
    obj.push(100)
    obj.push(200)
    obj.pop()
    param_3 = obj.top()
    assert param_3 == 100
    obj.push(1)
    param_4 = obj.getMin()
    assert param_4 == 1

    stack = MinStack()
    stack.push(-1)
    x = stack.top()
    assert x == -1
    x = stack.getMin()
    assert x == -1

    stack = MinStack()
    stack.push(2)
    stack.push(0)
    stack.push(3)
    stack.push(0)

    assert stack.getMin() == 0
    stack.pop()
    assert stack.getMin() == 0
    stack.pop()
    assert stack.getMin() == 0
    stack.pop()
    assert stack.getMin() == 2


if __name__ == '__main__':
    test()
