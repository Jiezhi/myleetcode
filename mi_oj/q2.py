#!/usr/bin/env python
"""
https://code.mi.com/problem/list/view?id=2
Created on 2018-12-24

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
    line = line.strip().split(' ')
    for l in line:
        if line.count(l) == 1:
            return l


if __name__ == '__main__':
    assert solution("10 10 11 12 12 11 16") == '16'
