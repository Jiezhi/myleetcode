#!/usr/bin/env python
"""
CREATED AT: 2022/4/7
Des:
https://leetcode.com/problems/implement-stack-using-queues/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import collections


class MyStack:
    """
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.

    16 / 16 test cases passed.
    Status: Accepted
    Runtime: 24 ms, faster than 98.8%
    Memory Usage: 14 MB, less than 29.43%
    """

    def __init__(self):
        self.preq = collections.deque()
        self.nextq = collections.deque()

    def push(self, x: int) -> None:
        self.nextq.append(x)

    def pop(self) -> int:
        while len(self.nextq) > 1:
            self.preq.append(self.nextq.popleft())
        if self.nextq:
            return self.nextq.popleft()
        else:
            while len(self.preq) > 1:
                self.nextq.append(self.preq.popleft())
            return self.preq.popleft()

    def top(self) -> int:
        ret = self.pop()
        self.nextq.append(ret)
        return ret

    def empty(self) -> bool:
        return len(self.nextq) == 0 and len(self.preq) == 0


def test():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert not stack.empty()


if __name__ == '__main__':
    test()
