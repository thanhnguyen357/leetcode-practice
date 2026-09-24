class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum3 = nums[l] + nums[r] + nums[i]
                if sum3 == 0:
                    ans.append([nums[l], nums[r], nums[i]])
                
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    r -= 1
        
        return ans
