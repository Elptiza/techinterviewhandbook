# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    in_beg = 0
    in_end = len(nums)-1
    start_ = nums[0]
    end_ = nums[len(nums)-1]
    result = []
    while in_beg <= in_end :
        print(in_beg, in_end)
        if start_*start_ > end_*end_:
            result.insert(0,start_*start_)
            in_beg +=1
            start_ = nums[in_beg]
        else:
            result.insert(0,end_*end_)
            in_end = in_end - 1
            end_ = nums[in_end]
    return print(result)

# Example 1:
nums = [-4,-1,0,3,10]
sortedSquares(nums)
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
