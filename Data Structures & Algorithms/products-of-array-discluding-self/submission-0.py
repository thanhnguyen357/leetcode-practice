class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        left_multi = 1
        for i in range(len(nums)):
            output[i] = left_multi
            left_multi *= nums[i]

        right_multi = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= right_multi
            right_multi *= nums[i]
        
        return output