class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for num in range(len(nums)):
            dic[nums[num]] = num
        
        for num in range(len(nums)):
            sec = target - nums[num]
            if sec in dic:
                return [num, dic[sec]]

