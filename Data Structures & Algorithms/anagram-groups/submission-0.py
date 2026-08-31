class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            sorted_text = "".join(sorted(word))
            
            if sorted_text not in dic:
                dic[sorted_text] = []

            dic[sorted_text].append(word)

        return list(dic.values())
