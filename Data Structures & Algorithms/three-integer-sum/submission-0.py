class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum3 = nums[left] + nums[right]
                if sum3 < target:
                    left += 1
                    if left == i:
                        left += 1
                elif sum3 > target:
                    right -= 1
                    if right == i:
                        right -= 1
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result