class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        count = [[] for i in range(len(nums) + 1)]

        for num, freq in hash_table.items():
            count[freq].append(num)
        
        ans = []
        for freq in range(len(count) - 1, 0, -1):
            if count[freq]:
                ans.extend(count[freq])
            
            if len(ans) == k:
                return ans

        