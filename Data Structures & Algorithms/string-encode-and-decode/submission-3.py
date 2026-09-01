class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string = encoded_string + f"{len(s)}" + '#' + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            word = ''
            j = i
            while s[j] != '#':
                j += 1
            step = int(s[i:j])
            word += s[j+1 : j+1+step]

            decoded_strs.append(word)
            
            i += step + 2
        
        return decoded_strs