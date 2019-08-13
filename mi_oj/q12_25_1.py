#!/usr/bin/env python
"""
Created on 2018-12-25

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # please write your code here
    if len(line) == 1:
        return 'true'
    nums = line.strip().split(' ')
    l = len(nums)
    ret = [0] * l
    for i in range(l):
        for j in range(int(nums[i])):
            if i + j + 1 >= l:
                break
            ret[i + j + 1] = 1
    print(ret)
    if 0 in ret[1:]:
        return 'false'
    else:
        return 'true'


# return 'your_answer'

if __name__ == '__main__':
    print(solution('0'))
    print(solution('0 1'))
    print(solution('2 0 1 0 0 3 4'))
    print(solution('5 0 0 0 0 0'))
