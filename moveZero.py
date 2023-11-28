class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        j = 0
        while j<n:
            if nums[j] == 0:
                j = j+1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i = i+1
                j = j+1