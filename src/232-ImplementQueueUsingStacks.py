#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:

https://leetcode.com/problems/implement-queue-using-stacks/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""


class MyQueue:
    """
    Runtime: 28 ms, faster than 94.99%
    Memory Usage: 14 MB, less than 34.78%

    1 <= x <= 9
    At most 100 calls will be made to push, pop, peek, and empty.
    All the calls to pop and peek are valid.
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0


def test():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()


if __name__ == '__main__':
    test()
