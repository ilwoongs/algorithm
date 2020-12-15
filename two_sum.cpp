//Given an array of integers, return the indices of the two numbers that add up to a given target

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result = {0,0};
        int leng = sizeof(nums)/6;
        
        for(int i=0;i<leng;i++){
            for(int j=i+1;j<leng;j++){
                if (nums[i]+nums[j] == target){
                    result[0] = i;
                    result[1] = j;
                }
            }
        }
        
        return result;
    }
        
  
};
