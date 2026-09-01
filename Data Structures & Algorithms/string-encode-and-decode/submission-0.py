class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string = encoded_string + f"{len(s)}" + '#' + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        j = i
        while i <= len(s):
            word = ''
    
            if s[i] == '#':
                step = int(s[j])
                j = i + 1
                for index in range(step):
                    word += s[j]
                    j += 1
                
                decoded_strs.append(word)
            
            i = j + 1
        
        return decoded_strs