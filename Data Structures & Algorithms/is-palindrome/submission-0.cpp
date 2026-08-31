class Solution {
public:
    bool isPalindrome(string s) {
         int left = 0, right = s.length();

         while(left <= right){
            if(s[left] < 48 || (s[left] > 57 && s[left] < 65) || (s[left] > 90 && s[left] < 97) || s[left] > 122){
                left ++;
                continue;
            }
            if(s[right] < 48 || (s[right] > 57 && s[right] < 65) || (s[right] > 90 && s[right] < 97) || s[right] > 122){
                right --;
                continue;
            }

            if(tolower(s[left]) != tolower(s[right])){
                return false;
            }

            left++;
            right--;
         }

         return true;
    }
};
