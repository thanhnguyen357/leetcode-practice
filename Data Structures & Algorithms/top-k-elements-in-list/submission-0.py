class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        count = [[] for i in range(len(nums) + 1)]
        
        for num, freq in hash_table.items():
            count[freq].append(num)
        ans = []

        for each in range(len(nums), 0, -1):
            ans.extend(count[each])
            
            if len(ans) == k:
                return ans
        

        