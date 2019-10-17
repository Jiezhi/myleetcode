#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019/10/17

Leetcode:  https://leetcode.com/problems/min-stack/

https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]

    def top(self) -> int:
        if self.stack:
            x = self.stack[len(self.stack) - 1]
            return x
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            m = self.stack[0]
            for i in self.stack:
                if i < m:
                    m = i
            return m
        else:
            return None


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
