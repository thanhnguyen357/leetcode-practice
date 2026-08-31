class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for num in range(len(nums)):
            dic[nums[num]] = num
        
        for num in range(len(nums)):
            sec = target - nums[num]
            if sec in dic and dic[sec] != num :
                return [num, dic[sec]]
            

