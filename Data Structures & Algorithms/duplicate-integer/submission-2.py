class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = {}
        for num in nums:
            if num in appear:
                return True
            else:
                appear[num] = 1
        
        return False