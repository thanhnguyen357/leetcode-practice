class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map <int, int> container;

        for(int i = 0; i < nums.size(); i++){
            container[target - nums[i]] = i;
        }
        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            if(container[nums[i]]){
                if(i == container[nums[i]]){
                    continue;
                }
                result.push_back(i);
                result.push_back(container[nums[i]]);
                return result;
            }
        }
        
    }
};
