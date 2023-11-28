# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

from collections import defaultdict
def two_sum (nums, target):
    comleteMap = defaultdict(int)
    for i in range(len(nums)):
        complete = target - nums[i]
        if nums[i] in comleteMap:
            return print([i,comleteMap[nums[i]]])
        else :
            comleteMap[complete] = i

def two_sum_long (nums, target):
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if target == nums[i]+nums[k]:
                return print([i, k])

nums = [2,7,11,15]
target = 9
two_sum(nums, target)
# nums = [3,2,4]
# target = 6
# # two_sum_long(nums, target)
# two_sum(nums, target)