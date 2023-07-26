class Solution:
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        right = [1] * len(nums)
        left_num = 1
        right_num = 1
        for i in range(1, len(nums)):
            left_num *= nums[i - 1]
            left[i] = left_num

        for i in range(len(nums) - 2, -1, -1):
            right_num *= nums[i + 1]
            right[i] = right_num

        for i in range(0, len(nums)):
            nums[i] = (right[i] * left[i])

        return nums


