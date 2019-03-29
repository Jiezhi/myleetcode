"""
 https://leetcode.com/problems/two-sum
 @Author: Jiezhi
 @Date: 2018-07-06 17:35:15 
 @Last Modified by:   Jiezhi
 @Last Modified time: 2018-07-06 17:35:15 
 """


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        result = target - nums[i]
        if result in nums[i + 1:]:
            return [i, i + 1 + nums[i + 1:].index(result)]


def test():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


if __name__ == '__main__':
    test()
