class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = []
        back = []
        for i in range(len(s)):
            if s[i].isalnum():
                front.append(s[i].lower())
            if s[len(s) - i - 1].isalnum():
                back.append(s[len(s) - i - 1].lower())
        
        return front == back