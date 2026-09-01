class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        
        return encoded_string
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_string = []
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            step = int(s[i:j])
            decoded_string.append(s[j+1: j + 1 + step])
            i = j + 1 +step
        
        return decoded_string
