class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        map<char, int> count;
        for(int i = 0; i < s.length(); i++){
            count[s[i]] ++;
        //}
       // for(int i = 0; i < t.length(); i++){
            count[t[i]] --;
        }
        for(int i = 0; i < s.length(); i++){
            if(count[s[i]] != 0){
                return false;
            }
        }

        return true;
    }
};
