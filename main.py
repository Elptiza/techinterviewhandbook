# # 15. 3Sum
# # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# #
# # Notice that the solution set must not contain duplicate triplets.
# #
from collections import defaultdict


def threeSum (nums):
    pre_result = defaultdict(int)
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] in pre_result:
                result.append([])
# - three sum
# - binary search (разные вариации)
# - max consequtive ones (I, II)
# - move zeroes
# - valid parenthesis

# # Example 1:
# # Input: nums = [-1, 0, 1, 2, -1, -4]
# # Output: [[-1, -1, 2], [-1, 0, 1]]
# # Explanation:
# # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# # The distinct triplets are [-1,0,1] and [-1,-1,2].
# # Notice that the order of the output and the order of the triplets does not matter.
# #
# # Example 2:
# #
# # Input: nums = [0, 1, 1]
# # Output: []
# # Explanation: The only possible triplet does not sum up to 0.
# #
# # Example 3:
# #
# # Input: nums = [0, 0, 0]
# # Output: [[0, 0, 0]]
# # Explanation: The only possible triplet sums up to 0.
# #
# nums = [-1, 0, 1, 2, -1, -4]
# threeSum(nums)
# # Output: [[-1, -1, 2], [-1, 0, 1]]


