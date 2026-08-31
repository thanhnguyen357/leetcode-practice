class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0, right =heights.size() - 1;
        int maxArea = 0;
        while(left < right){
            int container;
            if(heights[left] >= heights[right]){
                container = heights[right] * (right-left);
                right--;
            } else{
                container = heights[left] * (right-left);
                left++;
            }
            if(container > maxArea){
                maxArea = container;
            }
        }

        return maxArea; 
    }
};
